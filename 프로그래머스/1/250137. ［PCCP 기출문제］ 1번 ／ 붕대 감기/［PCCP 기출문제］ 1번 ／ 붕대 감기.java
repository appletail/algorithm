class Bandage {
    private int healStreak = 0;
    private int maxHealStreak;
    private int hps;
    private int healStreakBonus;
    
    public Bandage(int[] bandage) {
        this.maxHealStreak = bandage[0];
        this.hps = bandage[1];
        this.healStreakBonus = bandage[2];
    }
    
    public int heal() {
        this.healStreak += 1;
        int healValue = this.hps;
        if (this.healStreak == this.maxHealStreak) {
            healValue += this.healStreakBonus;
            this.healStreak = 0;
        }
        return healValue;
    }
    
    public void breakHealStreak() {
        this.healStreak = 0;
    }
}

class Health {
    private int health;
    private int maxHealth;
    
    public Health(int health) {
        this.health = health;
        this.maxHealth = health;
    }
    
    public int heal(int value) {
        this.health += value;
        if (this.health > this.maxHealth) {
            this.health = this.maxHealth;
        }
        return this.health;
    }
    
    public int damage(int value) {
        this.health -= value;
        if (this.health <= 0) {
            this.health = -1;
        }
        return this.health;
    }
    
    public int getHealth() {
        return this.health;
    }
}

class Monster {
    private int[][] attacks;
    private int attackCnt = 0;
    
    public Monster(int[][] attacks) {
        this.attacks = attacks;
    }
    
    public int nextAttackTime() {
        return this.attacks[this.attackCnt][0];
    }
    
    public int attack() {
        int damage = this.attacks[this.attackCnt][1];
        this.attackCnt += 1;
        return damage;
    }
    
    public int getLastAttackTime() {
        return this.attacks[this.attacks.length-1][0];
    }
}

class Game {
    private Bandage bandage;
    private Health playerHealth;
    private Monster monster;
    
    public Game(Bandage bandage, Health playerHealth, Monster monster) {
        this.bandage = bandage;
        this.playerHealth = playerHealth;
        this.monster = monster;
    }
    
    public void play() {
        int lastAttackTime = monster.getLastAttackTime();
        int time = 0;
        while (time < lastAttackTime) {
            time += 1;
            if (time != monster.nextAttackTime()) {
                playerHealth.heal(bandage.heal());
            } else {
                playerHealth.damage(monster.attack());
                bandage.breakHealStreak();
                if (playerHealth.getHealth() == -1) break;
            }
        }
    }
    
    public int getResult() {
        return playerHealth.getHealth();
    }
}

class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        Bandage playerBandage = new Bandage(bandage);
        Health playerHealth = new Health(health);
        Monster monster = new Monster(attacks);
        Game game = new Game(playerBandage, playerHealth, monster);
        game.play();
        
        return game.getResult();
    }
}