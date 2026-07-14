// ====================================================
// ДУХИ, що вільно літають і їх можна перетягувати мишкою/пальцем,
// як маленькі об'єкти в невагомості (космічна міні-гра).
//
// Логіка:
// - У кожного духа є "якірна" точка (звідки він стартує - береться
//   з CSS: top/left/right у .spirit-icon--N), і зміщення (x, y) від неї,
//   яке рухається через transform: translate3d(...).
// - Поки дух вільний, він повільно дрейфує зі своєю швидкістю (vx, vy),
//   трохи "тремтить" (випадкові поштовхи), і відбивається від країв екрану.
// - Коли дух перетягують - він точно слідує за курсором/пальцем.
// - Коли відпускають - зберігається швидкість останнього руху, і дух
//   "летить за інерцією" далі, поступово гальмуючи (тертя), доки знову
//   не почне тихо дрейфувати.
// ====================================================
(function () {
    'use strict';

    function initSpiritPhysics() {
        var spirits = document.querySelectorAll('.spirit-icon');
        if (!spirits.length) return;

        var FRICTION = 0.985;        // гальмування за кадр, коли дух летить за інерцією
        var IDLE_MAX_SPEED = 0.5;    // максимальна швидкість вільного дрейфу (px/кадр)
        var INERTIA_MAX_SPEED = 22;  // максимальна швидкість одразу після відпускання (px/кадр)
        var DRIFT_SMOOTH = 0.02;     // наскільки плавно швидкість "доганяє" ціль дрейфу (менше = плавніше, без тремтіння)

        var recalcFns = []; // функції перерахунку якоря кожного духа - викликаються при resize

        // Елементи-"перешкоди" - плашки/панелі, від яких духи мають відбиватися,
        // а не пролітати крізь них. Позначаються атрибутом data-spirit-obstacle
        // прямо в HTML-шаблонах (шапка сайту, центральна панель зі списком тощо).
        var obstacleEls = document.querySelectorAll('[data-spirit-obstacle]');

        function getObstacleRects() {
            var rects = [];
            obstacleEls.forEach(function (el) {
                var r = el.getBoundingClientRect();
                // Пропускаємо елементи, які зараз приховані (display: none),
                // напр. шапку чи панель на дуже вузьких екранах
                if (r.width > 0 && r.height > 0) rects.push(r);
            });
            return rects;
        }

        // AABB-колізія духа з прямокутником перешкоди: якщо перекриваються -
        // виштовхуємо духа назовні по осі найменшого проникнення і "відбиваємо"
        // відповідну складову швидкості (як від стінки)
        function resolveObstacle(state, anchor, rect) {
            var sLeft = anchor.left + state.x;
            var sTop = anchor.top + state.y;
            var sRight = sLeft + anchor.width;
            var sBottom = sTop + anchor.height;

            if (sRight <= rect.left || sLeft >= rect.right || sBottom <= rect.top || sTop >= rect.bottom) {
                return; // не перекриваються - нічого робити не треба
            }

            var overlapLeft = sRight - rect.left;
            var overlapRight = rect.right - sLeft;
            var overlapTop = sBottom - rect.top;
            var overlapBottom = rect.bottom - sTop;

            var minOverlapX = Math.min(overlapLeft, overlapRight);
            var minOverlapY = Math.min(overlapTop, overlapBottom);

            if (minOverlapX < minOverlapY) {
                if (overlapLeft < overlapRight) {
                    state.x -= overlapLeft;
                    state.vx = -Math.abs(state.vx || 0.1);
                } else {
                    state.x += overlapRight;
                    state.vx = Math.abs(state.vx || 0.1);
                }
            } else {
                if (overlapTop < overlapBottom) {
                    state.y -= overlapTop;
                    state.vy = -Math.abs(state.vy || 0.1);
                } else {
                    state.y += overlapBottom;
                    state.vy = Math.abs(state.vy || 0.1);
                }
            }
        }

        spirits.forEach(function (el, index) {
            el.classList.add('js-particle');

            // "Якірна" точка - позиція, яку елемент мав би БЕЗ transform
            // (задається в CSS через top/left/right). Читаємо її один раз,
            // до того як почнемо рухати елемент через transform.
            var anchor = el.getBoundingClientRect();

            var state = {
                x: 0, y: 0,
                vx: (Math.random() - 0.5) * IDLE_MAX_SPEED * 2,
                vy: (Math.random() - 0.5) * IDLE_MAX_SPEED * 2,
                dragging: false,
                pointerId: null,
                grabDX: 0, grabDY: 0,   // де саме на іконці схопили (щоб не "стрибала" під курсор)
                lastX: 0, lastY: 0,
                lastT: 0
            };

            function applyTransform() {
                el.style.transform = 'translate3d(' + state.x.toFixed(1) + 'px, ' + state.y.toFixed(1) + 'px, 0)';
            }

            function clampToViewport() {
                var minX = -anchor.left;
                var maxX = window.innerWidth - anchor.left - anchor.width;
                var minY = -anchor.top;
                var maxY = window.innerHeight - anchor.top - anchor.height;

                if (state.x < minX) { state.x = minX; state.vx = Math.abs(state.vx); }
                if (state.x > maxX) { state.x = maxX; state.vx = -Math.abs(state.vx); }
                if (state.y < minY) { state.y = minY; state.vy = Math.abs(state.vy); }
                if (state.y > maxY) { state.y = maxY; state.vy = -Math.abs(state.vy); }
            }

            function onPointerDown(e) {
                state.dragging = true;
                state.pointerId = e.pointerId;
                el.setPointerCapture(e.pointerId);
                el.classList.add('is-dragging');

                var rect = el.getBoundingClientRect();
                state.grabDX = e.clientX - rect.left;
                state.grabDY = e.clientY - rect.top;

                state.lastX = e.clientX;
                state.lastY = e.clientY;
                state.lastT = performance.now();

                e.preventDefault();
            }

            function onPointerMove(e) {
                if (!state.dragging || e.pointerId !== state.pointerId) return;

                var now = performance.now();
                var dt = Math.max(now - state.lastT, 1);

                // Нова абсолютна позиція лівого верхнього кута іконки
                var targetLeft = e.clientX - state.grabDX;
                var targetTop = e.clientY - state.grabDY;

                // Переводимо в зміщення відносно якірної точки
                state.x = targetLeft - anchor.left;
                state.y = targetTop - anchor.top;

                // Швидкість за останній рух - знадобиться для інерції після відпускання
                state.vx = (e.clientX - state.lastX) / dt * 16; // нормалізація приблизно під 60fps крок
                state.vy = (e.clientY - state.lastY) / dt * 16;

                state.lastX = e.clientX;
                state.lastY = e.clientY;
                state.lastT = now;

                applyTransform();
            }

            function onPointerUp(e) {
                if (e.pointerId !== state.pointerId) return;
                state.dragging = false;
                state.pointerId = null;
                el.classList.remove('is-dragging');

                // Обмежуємо швидкість інерції, щоб дух не вилітав за екран занадто різко
                var speed = Math.sqrt(state.vx * state.vx + state.vy * state.vy);
                if (speed > INERTIA_MAX_SPEED) {
                    var scale = INERTIA_MAX_SPEED / speed;
                    state.vx *= scale;
                    state.vy *= scale;
                }
            }

            el.addEventListener('pointerdown', onPointerDown);
            el.addEventListener('pointermove', onPointerMove);
            el.addEventListener('pointerup', onPointerUp);
            el.addEventListener('pointercancel', onPointerUp);

            // Унікальний фазовий зсув і частоти для кожного духа, щоб вони не рухались
            // синхронно і щоб траєкторія виглядала органічно, а не по колу
            var seed = index * 12.9898;
            var freqX1 = 0.00013 + (index % 5) * 0.00003;
            var freqX2 = 0.00021 + (index % 7) * 0.00002;
            var freqY1 = 0.00017 + (index % 4) * 0.00004;
            var freqY2 = 0.00026 + (index % 6) * 0.00002;

            function tick() {
                if (!state.dragging) {
                    var t = performance.now();

                    // ПЛАВНИЙ дрейф: замість випадкових поштовхів щокадру (що і давало
                    // "тремтіння"), ціль швидкості обчислюється як сума кількох плавних
                    // синусоїд з різними періодами і фазою для кожного духа. Це дає
                    // безкінечно плавну, неповторювану "живу" траєкторію без різких змін.
                    var targetVx = (Math.sin(seed + t * freqX1) + Math.sin(seed * 1.7 + t * freqX2)) * (IDLE_MAX_SPEED * 0.5);
                    var targetVy = (Math.cos(seed * 1.3 + t * freqY1) + Math.sin(seed * 2.1 + t * freqY2)) * (IDLE_MAX_SPEED * 0.5);

                    // Тертя - гасить швидкість, набуту від перетягування (інерцію)
                    state.vx *= FRICTION;
                    state.vy *= FRICTION;

                    // Плавно "доганяємо" ціль дрейфу (лінійна інтерполяція),
                    // а не стрибаємо до неї - це і прибирає тремтіння
                    state.vx += (targetVx - state.vx) * DRIFT_SMOOTH;
                    state.vy += (targetVy - state.vy) * DRIFT_SMOOTH;

                    var speed = Math.sqrt(state.vx * state.vx + state.vy * state.vy);
                    if (speed > IDLE_MAX_SPEED) {
                        var scale = IDLE_MAX_SPEED / speed;
                        state.vx *= scale;
                        state.vy *= scale;
                    }

                    state.x += state.vx;
                    state.y += state.vy;

                    // Відбій від плашок/панелей (шапка, центральний контейнер тощо),
                    // а тільки потім - від країв екрану
                    var obstacles = getObstacleRects();
                    for (var i = 0; i < obstacles.length; i++) {
                        resolveObstacle(state, anchor, obstacles[i]);
                    }

                    clampToViewport();
                    applyTransform();
                }

                requestAnimationFrame(tick);
            }

            requestAnimationFrame(tick);

            // Реєструємо функцію перерахунку якоря саме цього духа
            recalcFns.push(function () {
                var prevTransform = el.style.transform;
                el.style.transform = 'none';
                anchor = el.getBoundingClientRect();
                el.style.transform = prevTransform;
            });
        });

        // При зміні розміру вікна перераховуємо якорі, щоб духи не "застрягали"
        // за межами нового вікна
        window.addEventListener('resize', function () {
            recalcFns.forEach(function (fn) { fn(); });
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSpiritPhysics);
    } else {
        initSpiritPhysics();
    }
})();
