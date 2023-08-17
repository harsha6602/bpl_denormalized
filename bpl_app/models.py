from django.db import models

# Create your models here.

class TeamsInfo(models.Model):
    team_id = models.CharField(max_length=128,unique=True)
    player_id = models.CharField(max_length=12,unique=True)
    primary_together = (team_id,player_id)
    team_name = models.CharField(max_length=128,unique=True)
    captain_phoneno = models.CharField(max_length=12)
    player_role = models.CharField(max_length=128,null=True)
    phone_no = models.CharField(max_length=12,unique=True)
    branch = models.CharField(max_length=128)
    player_name = models.CharField(max_length=128,null=True)
    sport = models.CharField(max_length=12,default="null")

    # class Meta:
    #     db_table = 'Team_primary'


    def __str__(self):
        return self.team_id

class Matches(models.Model):
    match_no = models.CharField(max_length=12,unique=True,primary_key=True)
    team1_id = models.CharField(max_length=128,unique=True)
    team2_id = models.CharField(max_length=128,unique=True)
    umpire_name = models.CharField(max_length=128,default="none")
    runs = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    status = models.CharField(max_length=128)
    overs = models.IntegerField(default=0)
    
    def __str__(self):
        return self.match_no
