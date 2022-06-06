import settings

def height_prct(precentage):
    return (settings.HEIGHT / 100) * precentage

def width_prct(precentage):
    return (settings.WIDTH / 100) * precentage

if __name__ == "__main__":
    print(height_prct(25))
