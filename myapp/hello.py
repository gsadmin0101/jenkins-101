import fire

def hello(name="World"):
  return "Olá %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)