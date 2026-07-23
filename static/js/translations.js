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
    show_more: {
        en: "Show more",
        de: "Mehr anzeigen",
        es: "Mostrar más",
        ja: "もっと見る"
    },
    show_less: {
        en: "Show less",
        de: "Weniger anzeigen",
        es: "Mostrar menos",
        ja: "少なく表示"
    },
    form_base: {
        en: "Base Form",
        de: "Grundform",
        es: "Forma base",
        ja: "基本形態"
    },
    abilities_page_title: {
        en: "Abilities",
        de: "Fähigkeiten",
        es: "Habilidades",
        ja: "能力"
    },
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
    },

    /* ===== Таблиця статів на сторінці окремого кота (cat_detail.html) ===== */
    stats_section_main: {
        en: "Stats",
        de: "Statuswerte",
        es: "Estadísticas",
        ja: "ステータス"
    },
    traits_title: {
        en: "Traits",
        de: "Merkmale",
        es: "Rasgos",
        ja: "特性"
    },
    abilities_title: {
        en: "Abilities",
        de: "Fähigkeiten",
        es: "Habilidades",
        ja: "特殊能力"
    },
    stats_section_speed: {
        en: "Attack Speed & Recharge",
        de: "Angriffstempo & Wiederaufladung",
        es: "Velocidad de ataque y recarga",
        ja: "攻撃速度と再出撃時間"
    },
    stats_section_economy: {
        en: "Battle Economy",
        de: "Kampfwirtschaft",
        es: "Economía de batalla",
        ja: "バトルコスト"
    },
    stat_hp: {
        en: "Health",
        de: "Gesundheit",
        es: "Salud",
        ja: "体力"
    },
    stat_attack_power: {
        en: "Attack Power",
        de: "Angriffskraft",
        es: "Poder de ataque",
        ja: "攻撃力"
    },
    stat_dps: {
        en: "Damage Per Second (DPS)",
        de: "Schaden pro Sekunde (DPS)",
        es: "Daño por segundo (DPS)",
        ja: "秒間ダメージ（DPS）"
    },
    stat_knockbacks: {
        en: "Knockbacks",
        de: "Rückstöße",
        es: "Retrocesos",
        ja: "ノックバック回数"
    },
    stat_range: {
        en: "Range",
        de: "Reichweite",
        es: "Alcance",
        ja: "射程距離"
    },
    stat_speed: {
        en: "Movement Speed",
        de: "Bewegungsgeschwindigkeit",
        es: "Velocidad de movimiento",
        ja: "移動速度"
    },
    stat_attack_frequency: {
        en: "Attack Frequency",
        de: "Angriffsfrequenz",
        es: "Frecuencia de ataque",
        ja: "攻撃頻度"
    },
    stat_foreswing: {
        en: "Foreswing",
        de: "Vorschwung",
        es: "Preataque (Foreswing)",
        ja: "予備動作"
    },
    stat_recharge: {
        en: "Recharge Time",
        de: "Wiederaufladezeit",
        es: "Tiempo de recarga",
        ja: "再出撃時間"
    },
    stat_cost: {
        en: "Summon Cost",
        de: "Beschwörungskosten",
        es: "Costo de invocación",
        ja: "出撃コスト"
    },
    stat_cost_default: {
        en: "Default Price",
        de: "Standardpreis",
        es: "Precio predeterminado",
        ja: "初期コスト"
    },
    unit_times: {
        en: "times",
        de: "Mal",
        es: "veces",
        ja: "回"
    },
    unit_melee_single: {
        en: "Melee, single target",
        de: "Nahkampf, Einzelziel",
        es: "Cuerpo a cuerpo, objetivo único",
        ja: "近距離・単体攻撃"
    },
    unit_every: {
        en: "every",
        de: "alle",
        es: "cada",
        ja: "毎"
    },
    unit_seconds: {
        en: "sec.",
        de: "Sek.",
        es: "seg.",
        ja: "秒"
    },
    unit_from: {
        en: "from",
        de: "von",
        es: "desde",
        ja: "最短"
    },
    unit_to: {
        en: "to",
        de: "bis",
        es: "hasta",
        ja: "〜最長"
    },
    unit_recharge_note: {
        en: "Depends on Cat Cannon / base level upgrades",
        de: "Abhängig von Katzenkanone / Basis-Upgrades",
        es: "Depende del Cañón Gatuno / mejoras de base",
        ja: "キャノン砲・本部レベルの強化状況による"
    },
    unit_chapter: {
        en: "Chapter",
        de: "Kapitel",
        es: "Capítulo",
        ja: "章"
    },
    unit_knockbacks_short: {
        en: "Knockbacks",
        de: "Rückstöße",
        es: "Retrocesos",
        ja: "ノックバック"
    },
    unit_damage: {
        en: "Damage",
        de: "Schaden",
        es: "Daño",
        ja: "ダメージ"
    },
    unit_speed_note: {
        en: "Movement speed",
        de: "Bewegungsgeschwindigkeit",
        es: "Velocidad de movimiento",
        ja: "移動速度"
    },
    unit_dps_short: {
        en: "DPS",
        de: "DPS",
        es: "DPS",
        ja: "DPS"
    },
    unit_seconds_short: {
        en: "s",
        de: "s",
        es: "s",
        ja: "秒"
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

    // Динамічний переклад - для тексту з БАЗИ ДАНИХ (ім'я й опис конкретного
    // кота), а не зі словника DICTIONARY. Кожен такий елемент сам носить свої
    // переклади в data-de/data-es/data-ja/data-en (їх виводить Django-шаблон
    // з полів title_de, content_de і т.д.). Якщо перекладу для мови нема -
    // просто лишаємо англійську версію (data-en), яку завжди підставляє сервер.
    document.querySelectorAll('.i18n-dynamic').forEach(function (el) {
        var translated = el.getAttribute('data-' + langCode);
        if (translated) {
            el.textContent = translated;
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
