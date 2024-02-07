velocidade = 61
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if(velocidade > RADAR_1 and local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)):
    print('Velocidade máx ultrapassada')
else:
    print('Dentro da velocidade')