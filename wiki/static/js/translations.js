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
        ja: "データベースに猫의データが見つかりませんでした。管理パネルから猫を追加してください！"
    },
    back_to_main: {
        en: "← Back to Main Page",
        de: "← Zurück zur Hauptseite",
        es: "← Volver a la página principal",
        ja: "← メインページに戻る"
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
    // ПОВНИЙ ПЕРЕКЛАД ДЛЯ ТВОЇХ КНОПОК РІД КІСНОСТЕЙ ЗІ СКРИНШОТУ:
    rarity_normal: {
        en: "Normal Cats",
        de: "Normale Katzen",
        es: "Gatos Normales",
        ja: "基本キャラ"
    },
    rarity_special: {
        en: "Special Cats",
        de: "Spezial-Katzen",
        es: "Gatos Especiales",
        ja: "EXキャラ"
    },
    rarity_rare: {
        en: "Rare Cats",
        de: "Seltene Katzen",
        es: "Gatos Raros",
        ja: "レアキャラ"
    },
    rarity_super_rare: {
        en: "Super Rare Cats",
        de: "Superseltene Katzen",
        es: "Gatos Súper Raros",
        ja: "激レアキャラ"
    },
    rarity_uber: {
        en: "Uber Rare Cats",
        de: "Uber-seltene Katzen",
        es: "Gatos Uber Raros",
        ja: "超激レアキャラ"
    },
    rarity_legend: {
        en: "Legend Rare Cats",
        de: "Legendäre seltene Katzen",
        es: "Gatos Leyenda Raros",
        ja: "伝説レアキャラ"
    },
    rarity_limited: {
        en: "Limited Cats",
        de: "Limitierte Katzen",
        es: "Gatos Limitados",
        ja: "限定キャラ"
    }
};

const LANG_BUTTON_LABELS = { en: "EN ▾", de: "DE ▾", es: "ES ▾", ja: "JA ▾" };

function setLanguage(langCode) {
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
        var key = el.getAttribute('data-i18n');
        if (DICTIONARY[key] && DICTIONARY[key][langCode]) {
            el.textContent = DICTIONARY[key][langCode];
        }
    });

    var langBtn = document.getElementById('langBtn');
    if (langBtn) {
        langBtn.textContent = LANG_BUTTON_LABELS[langCode];
    }

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

    localStorage.setItem('chosenLang', langCode);
}

document.addEventListener('click', function (event) {
    var switchBlock = document.querySelector('.lang-switch');
    if (switchBlock && !switchBlock.contains(event.target)) {
        var dropdown = document.getElementById('langDropdown');
        if (dropdown) {
            dropdown.classList.remove('open');
        }
    }
});

document.addEventListener('DOMContentLoaded', function () {
    var savedLang = localStorage.getItem('chosenLang');
    if (savedLang) {
        setLanguage(savedLang);
    }
});
