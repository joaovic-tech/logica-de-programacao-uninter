from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:
    # usando o underline duas vezes no python significa que esse método é protegido
    # Só pode ser usando na classe EntityMediator

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __print_collision_info(ent1, ent2):
        """Exibe informações sobre a colisão entre duas entidades."""
        print()
        print(f"{ent1.name} colidiu com {ent2.name}")
        print(f"Vida do {ent1.name}: {ent1.health}")
        print(f"Vida do {ent2.name}: {ent2.health}")

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        # Verificar se a interação entre as entidades é válida
        if (
                isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot)) or (
                isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy)) or (
                isinstance(ent1, Player) and isinstance(ent2, EnemyShot)) or (
                isinstance(ent1, EnemyShot) and isinstance(ent2, Player)) or (
                isinstance(ent1, Enemy) and isinstance(ent2, Player)) or (
                isinstance(ent1, Player) and isinstance(ent2, Enemy)
        ):

            # Usar colliderect (pygame) para verificar colisão
            if ent1.rect.colliderect(ent2.rect):
                # Aplicar dano conforme a lógica do jogo
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

                # Exibir informações de colisão
                EntityMediator.__print_collision_info(ent1, ent2)

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score

        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)

            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(ent1=entity1, ent2=entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
