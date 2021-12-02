import re

English= 'She is a vegetarian. '
English+= 'She does not eat meat.'
English+= 'She is thinks that animals should not be killed. '
English+= 'It is hard for her to hang out with people.'
English+= 'Many people like to eat meat. '
English+= 'She told his parents not to have meat.'
English+= 'They laughed at her. She realized they couldn\'t give up meat.'

Koren= '그녀는 채식주의자입니다.'
Koren+= '그녀는 고기를 먹지 않습니다.'
Koren+= '그녀는 동물을 죽이지 말아야한다고 생각합니다.'
Koren+= '그녀가 사람들과 어울리는 것은 어렵습니다. '
Koren+= '많은 사람들이 고기를 좋아합니다. '
Koren+= '그녀는 부모에게 고기를 먹지 말라고 말했습니다. '
Koren+= '그들은 그녀를 비웃었습니다.'
Koren+= '그녀는 그들이 고기를 포기하지 않을 것이라는 것을 깨달았습니다.'

print(English)
print(len(English))

print(Koren)
print(len(Koren))

Koren_list= re.split('\.', Koren)
print(Koren_list)
English_list= re.split('\.', English)
print(English_list)

total= []
 #영어+한글 리스트를 total 리스트에 넣고 출력
for i in range(len(English_list)):
   total.append([English_list[i],Koren_list[i]])

print(total)
