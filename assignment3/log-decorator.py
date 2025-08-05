#%%
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
  def wrapper(*args, **kwargs):
    logger.log(logging.INFO, f"Function: {func.__name__}\n"
                             f"Positional parameters: {args if args else "none"}\n"
                             f"Keyword Paramenters: {kwargs if kwargs else "none"}\n"
               )
    func()
  return wrapper

@logger_decorator
def calm_jojo():
  print("It's okay Joleeeeene")

@logger_decorator
def add_em_up(*nums):
  print(sum(nums))
  return True

@logger_decorator
def write_a_dict(**dict):
  for key, value in dict.items():
    print(f"My {key} is a {value}")

calm_jojo()
add_em_up(2,3,5)
write_a_dict({
  "pet": "cat",
  "age": 40,
  "foot": "warm"
})
#%%