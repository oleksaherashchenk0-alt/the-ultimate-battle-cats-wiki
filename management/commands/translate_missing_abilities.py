"""
Одноразова команда: заповнює переклади (DE/ES/JA) для 4 здібностей,
які були додані вже після відновлення бази з GitHub і лишились без
перекладу (Colossus Slayer, Immune to Curse, Long Range, Omni Strike).
Безпечно запускати повторно - просто перезапише ці ж 4 записи тими
самими значеннями, нічого іншого не чіпає.

Використання:
    python manage.py translate_missing_abilities
"""
from django.core.management.base import BaseCommand
from wiki.models import Ability

DATA = {
    "Colossus Slayer": {
        "name_de": "Kolossus-Bezwinger",
        "name_es": "Verdugo de Colosos",
        "name_ja": "コロッサススレイヤー",
        "description_de": "Diese Kampffähigkeit verleiht Einheiten einzigartige taktische Vorteile im Kampf gegen massive Colossus-Gegner. Katzen mit dieser Eigenschaft verursachen zwanzig Prozent mehr Schaden gegen jeden Colossus-Feind und reduzieren gleichzeitig den eingehenden Schaden von ihnen um dreißig Prozent. Diese Kombination erhöht deutlich sowohl die Überlebenszeit als auch den Gesamtschaden der Einheit bei Begegnungen mit riesigen Bossen. Wurde in Version 11.4 hinzugefügt.",
        "description_es": "Esta habilidad de combate otorga a las unidades ventajas tácticas únicas al enfrentarse a enemigos masivos de tipo Coloso. Los gatos con este rasgo infligen un veinte por ciento más de daño a cualquier enemigo Coloso, mientras reducen en un treinta por ciento el daño que reciben de ellos. Esta combinación aumenta notablemente tanto el tiempo de supervivencia como el daño total durante los enfrentamientos con jefes gigantes. Se añadió en la versión 11.4.",
        "description_ja": "この戦闘能力は、巨大なコロッサス系の敵と戦う際にユニットへ独自の戦術的優位性を与える。この特性を持つ猫は、コロッサス敵に対して20%多くダメージを与えると同時に、受けるダメージを30%軽減する。この組み合わせにより、巨大ボス戦での生存時間と総ダメージ量の両方が大幅に向上する。バージョン11.4で追加された。",
    },
    "Immune to Curse": {
        "name_de": "Immun gegen Fluch",
        "name_es": "Inmune a la Maldición",
        "name_ja": "呪い無効",
        "description_de": "Diese passive Fähigkeit verleiht bestimmten Katzen vollständigen Schutz vor dem Fluch-Effekt des Gegners. Wird eine Einheit mit dieser Immunität von einem fluchenden Angriff getroffen, negiert sie den Debuff vollständig und kann so ununterbrochen all ihre ursprünglichen Eigenschaften, Fähigkeiten und biologischen Vorteile weiter auslösen. Wurde in Version 7.0 hinzugefügt.",
        "description_es": "Esta habilidad pasiva otorga a gatos específicos protección total contra el efecto de maldición del enemigo. Cuando una unidad con esta inmunidad recibe un golpe maldecido, anula por completo el debuff, permitiéndole seguir activando sin interrupción todos sus rasgos, habilidades y ventajas biológicas originales. Se añadió en la versión 7.0.",
        "description_ja": "このパッシブ能力は、特定の猫に敵の呪い効果への完全な耐性を与える。この耐性を持つユニットが呪いの攻撃を受けても、デバフを完全に無効化し、元々持つ特性・能力・生物学的優位性を中断なく発動し続けられる。バージョン7.0で追加された。",
    },
    "Long Range": {
        "name_de": "Langstrecke",
        "name_es": "Largo Alcance",
        "name_ja": "遠距離攻撃",
        "description_de": "Dieser Kampfmechanismus ermöglicht es bestimmten Katzen, Ziele in einer festgelegten Zone weiter hinten auf dem Schlachtfeld zu treffen. Zwar können Einheiten dadurch sicher aus dem Hintergrund entfernte Gegner treffen, doch entsteht direkt vor der Katze ein deutlicher toter Winkel, in dem sie keinen Schaden verursachen kann, falls Gegner die Mindestreichweite unterschreiten. Wurde in Version 5.0 hinzugefügt.",
        "description_es": "Este mecanismo de combate permite a ciertos gatos golpear objetivos ubicados en una zona designada más alejada del campo de batalla. Aunque permite atacar con seguridad a enemigos distantes desde la retaguardia, crea un notable punto ciego justo delante del gato, donde no puede infligir daño si los oponentes logran superar el umbral de alcance mínimo. Se añadió en la versión 5.0.",
        "description_ja": "この戦闘メカニズムにより、特定の猫は戦場の奥にある指定エリア内の敵を攻撃できる。後方から安全に遠くの敵を攻撃できる一方、敵が最低射程のしきい値を突破すると、猫のすぐ前に大きな死角が生まれ、そこではダメージを与えられなくなる。バージョン5.0で追加された。",
    },
    "Omni Strike": {
        "name_de": "Rundumschlag",
        "name_es": "Golpe Omnidireccional",
        "name_ja": "オムニストライク",
        "description_de": "Dieser Kampfmechanismus erlaubt es bestimmten Katzen, eine vollständige Radialzone sowohl vor als auch hinter ihrer physischen Position zu treffen. Anders als gewöhnliche Fernkampf-Einheiten, die direkt neben sich einen toten Winkel haben, fegt ein Rundumschlag über den gesamten festgelegten kreisförmigen Bereich - dadurch können vergrabene Zombies oder Frontgegner, die tief in die Reichweite der Katze vorgedrungen sind, leicht beseitigt werden. Wurde in Version 7.0 hinzugefügt.",
        "description_es": "Este mecanismo de combate permite a ciertos gatos golpear una zona radial completa que se extiende tanto delante como detrás de su posición física. A diferencia de las unidades de largo alcance estándar, que tienen puntos ciegos justo a su lado, un Golpe Omnidireccional barre toda el área circular designada, lo que le permite eliminar fácilmente Zombies enterrados o enemigos de primera línea que hayan avanzado profundamente en su alcance. Se añadió en la versión 7.0.",
        "description_ja": "この戦闘メカニズムにより、特定の猫は自分の位置の前後両方に広がる全方位ゾーンを攻撃できる。すぐ横に死角がある通常の遠距離ユニットとは異なり、オムニストライクは指定された円形エリア全体を薙ぎ払うため、埋伏したゾンビや射程の内側深くまで入り込んだ前線の敵も簡単に一掃できる。バージョン7.0で追加された。",
    },
}


class Command(BaseCommand):
    help = "Заповнює переклади для здібностей, доданих після відновлення бази"

    def handle(self, *args, **options):
        updated = 0
        missing = []
        for name, data in DATA.items():
            try:
                ability = Ability.objects.get(name=name)
            except Ability.DoesNotExist:
                missing.append(name)
                continue
            for field, value in data.items():
                setattr(ability, field, value)
            ability.save()
            updated += 1
            self.stdout.write(self.style.SUCCESS(f"Перекладено: {name}"))
        if missing:
            self.stdout.write(self.style.WARNING(f"Не знайдено в базі (пропущено): {missing}"))
        self.stdout.write(self.style.SUCCESS(f"Готово, оновлено: {updated}"))
