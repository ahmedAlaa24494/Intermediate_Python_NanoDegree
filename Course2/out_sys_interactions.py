import subprocess
import random


p = subprocess.run(['emoj', 'dog'], stdout=subprocess.PIPE)
emoji = p.stdout.decode('utf-8').split(' ')
print(random.choice(emoji))


# p = subprocess.Popen(['ls'], stdout=subprocess.PIPE)
# output, err = p.communicate()
# p_status = p.wait()

# emoji = output.decode('utf-8').split(' ')

# print(random.choice(emoji))