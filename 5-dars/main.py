import decorators

# Pastda 4 ta decorator berilgan. Decorators faylida birin-ketinligi keltirilgan

# @decorators.checker
# @decorators.check
# @decorators.time_returner
@decorators.time_between
def salom_ber(ism):
    return f"Assalomu alaykum {ism}"

print(salom_ber(input('Ismingiz nima? ')))