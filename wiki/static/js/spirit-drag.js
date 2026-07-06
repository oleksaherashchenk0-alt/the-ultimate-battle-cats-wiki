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
        var IDLE_JITTER = 0.05;      // сила випадкових поштовхів під час вільного дрейфу
        var IDLE_MAX_SPEED = 0.5;    // максимальна швидкість вільного дрейфу (px/кадр)
        var INERTIA_MAX_SPEED = 22;  // максимальна швидкість одразу після відпускання (px/кадр)

        var recalcFns = []; // функції перерахунку якоря кожного духа - викликаються при resize

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

            // Невеличкий випадковий фазовий зсув, щоб духи не рухались синхронно
            var seed = index * 12.9898;

            function tick() {
                if (!state.dragging) {
                    // Легкий випадковий поштовх - імітація дрейфу в невагомості
                    state.vx += (Math.random() - 0.5) * IDLE_JITTER;
                    state.vy += (Math.random() - 0.5) * IDLE_JITTER;

                    // Тертя - гасить швидкість, набуту від перетягування, до спокійного дрейфу
                    state.vx *= FRICTION;
                    state.vy *= FRICTION;

                    var speed = Math.sqrt(state.vx * state.vx + state.vy * state.vy);
                    if (speed > IDLE_MAX_SPEED) {
                        var scale = IDLE_MAX_SPEED / speed;
                        state.vx *= scale;
                        state.vy *= scale;
                    } else if (speed < 0.05) {
                        // Ніколи не завмирає повністю - завжди тихо "плаває"
                        state.vx += Math.cos(seed + performance.now() * 0.0002) * 0.01;
                        state.vy += Math.sin(seed + performance.now() * 0.00025) * 0.01;
                    }

                    state.x += state.vx;
                    state.y += state.vy;

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
