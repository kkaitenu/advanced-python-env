def is_alive(health):
    if health <= 0:
        return False
    else:
        return True

print(is_alive(-5))