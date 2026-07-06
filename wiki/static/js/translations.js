/* ====================================================
   ВЛАСНИЙ СЛОВНИК-ПЕРЕКЛАД (без Google Translate, без банера,
   без інтернету). Один файл для УСІХ сторінок сайту.
   Кожен ключ -> переклад на 4 мови.

   ЯК ДОДАТИ ПЕРЕКЛАД НОВОГО ТЕКСТУ (на будь-якій сторінці):
   1. У HTML додай атрибут data-i18n="свій_ключ" на потрібний елемент
   2. Тут, у DICTIONARY, додай новий рядок з тим самим ключем і перекладами
   Працює однаково на index.html, units_menu.html і будь-якій новій сторінці -
   досить підключити цей файл через <script src="{% static 'js/translations.js' %}">
==================================================== */

const DICTIONARY = {
    site_title: {
        en: "The Battle Cats Wiki",
        de: "Das Battle Cats Wiki",
        es: "La Wiki de Battle Cats",
        ja: "バトルキャッツウィキ"
    },
    site_subtitle: {
        en: "Welcome to the cat encyclopedia. | By: Huki",
        de: "Willkommen in der Katzen-Enzyklopädie. | Von: Huki",
        es: "Bienvenido a la enciclopedia felina. | Por: Huki",
        ja: "猫百科事典へようこそ。| 作成者：Huki"
    },
    cat_dictionary: {
        en: "Units",
        de: "Einheiten",
        es: "Unidades",
        ja: "ユニット"
    },
    rarity_label: {
        en: "Rarity:",
        de: "Seltenheit:",
        es: "Rareza:",
        ja: "レア度："
    },
    desc_strategy: {
        en: "Description & Strategy:",
        de: "Beschreibung & Strategie:",
        es: "Descripción y Estrategia:",
        ja: "説明と戦略："
    },
    author_label: {
        en: "Author:",
        de: "Autor:",
        es: "Autor:",
        ja: "作者："
    },
    no_cats_found: {
        en: "No cats found in the database. Go to admin panel to add some!",
        de: "Keine Katzen in der Datenbank gefunden. Geh ins Admin-Panel, um welche hinzuzufügen!",
        es: "No se encontraron gatos en la base de datos. ¡Ve al panel de administración para añadir algunos!",
        ja: "データベースに猫のデータが見つかりませんでした。管理パネルから猫を追加してください！"
    },
    back_to_main: {
        en: "← Back to Main Page",
        de: "← Zurück zur Hauptseite",
        es: "← Volver a la página principal",
        ja: "← メインページに戻る"
    },
    back_short: {
        en: "← Back",
        de: "← Zurück",
        es: "← Volver",
        ja: "← 戻る"
    },
    units_catalog_title: {
        en: "Cat Units Catalog",
        de: "Katzen-Einheiten-Katalog",
        es: "Catálogo de Unidades de Gatos",
        ja: "猫ユニットカタログ"
    },
    no_cats_found_units: {
        en: "No cats found. Go to admin panel to add units!",
        de: "Keine Katzen gefunden. Geh ins Admin-Panel, um Einheiten hinzuzufügen!",
        es: "No se encontraron gatos. ¡Ve al panel de administración para añadir unidades!",
        ja: "猫が見つかりませんでした。管理パネルからユニットを追加してください！"
    },
    rarity_normal: {
        en: "Normal Cats",
        de: "Normale Katzen",
        es: "Gatos Normales",
        ja: "ノーマルキャット"
    },
    rarity_special: {
        en: "Special Cats",
        de: "Spezielle Katzen",
        es: "Gatos Especiales",
        ja: "スペシャルキャット"
    },
    rarity_rare: {
        en: "Rare Cats",
        de: "Seltene Katzen",
        es: "Gatos Raros",
        ja: "レアキャット"
    },
    rarity_super_rare: {
        en: "Super Rare Cats",
        de: "Superseltene Katzen",
        es: "Gatos Super Raros",
        ja: "激レアキャット"
    },
    rarity_uber: {
        en: "Uber Rare Cats",
        de: "Uber-seltene Katzen",
        es: "Gatos Uber Raros",
        ja: "超激レアキャット"
    },
    rarity_legend: {
        en: "Legend Rare Cats",
        de: "Legendäre Katzen",
        es: "Gatos Legendarios",
        ja: "伝説レアキャット"
    },
    rarity_limited: {
        en: "Limited Cats",
        de: "Limitierte Katzen",
        es: "Gatos Limitados",
        ja: "期間限定キャット"
    },
    rarity_panel_coming_soon: {
        en: "Cats of this rarity will appear here soon!",
        de: "Katzen dieser Seltenheit erscheinen hier bald!",
        es: "¡Los gatos de esta rareza aparecerán aquí pronto!",
        ja: "このレア度の猫は近日公開予定です！"
    }
};

const LANG_BUTTON_LABELS = { en: "EN ▾", de: "DE ▾", es: "ES ▾", ja: "JA ▾" };

// Головна функція перемикання мови: пробігає по всіх елементах
// з data-i18n і підставляє переклад з DICTIONARY. Працює на будь-якій
// сторінці, яка підключила цей файл і має ці самі id/класи в шапці.
function setLanguage(langCode) {
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
        var key = el.getAttribute('data-i18n');
        if (DICTIONARY[key] && DICTIONARY[key][langCode]) {
            el.textContent = DICTIONARY[key][langCode];
        }
    });

    // Текст на самій кнопці вибору мови (EN ▾ / DE ▾ / ...)
    var langBtn = document.getElementById('langBtn');
    if (langBtn) {
        langBtn.textContent = LANG_BUTTON_LABELS[langCode];
    }

    // Виправлення шрифту для японської: контур Impact ламає ієрогліфи,
    // тому для японської вмикаємо інший, "рідний" для кандзі шрифт.
    // querySelectorAll - бо клас battle-cats-font може бути на кількох
    // елементах різних сторінок (наприклад заголовок "Cat Units Catalog")
    document.querySelectorAll('.battle-cats-font, #catDictBtnText').forEach(function (el) {
        if (langCode === 'ja') {
            el.classList.add('jp-text');
        } else {
            el.classList.remove('jp-text');
        }
    });

    document.documentElement.setAttribute('lang', langCode);

    var dropdown = document.getElementById('langDropdown');
    if (dropdown) {
        dropdown.classList.remove('open');
    }

    // Запам'ятовуємо вибір мови, щоб він лишався після переходу на іншу
    // сторінку сайту і після перезавантаження
    localStorage.setItem('chosenLang', langCode);
}

// Закриваємо список мов, якщо клікнули будь-де поза ним
document.addEventListener('click', function (event) {
    var switchBlock = document.querySelector('.lang-switch');
    if (switchBlock && !switchBlock.contains(event.target)) {
        var dropdown = document.getElementById('langDropdown');
        if (dropdown) {
            dropdown.classList.remove('open');
        }
    }
});

// При завантаженні БУДЬ-ЯКОЇ сторінки застосовуємо мову, яку людина
// обрала минулого разу - саме це робить переклад "наскрізним" по сайту
document.addEventListener('DOMContentLoaded', function () {
    var savedLang = localStorage.getItem('chosenLang');
    if (savedLang) {
        setLanguage(savedLang);
    }
});
