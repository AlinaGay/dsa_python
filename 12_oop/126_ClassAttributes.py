class StarCookie:
  def __init__(self, color, weight):
    # initialaze attributes
    print("The cookie is ready")
    self.color = color
    self.weight = weight

star_cookie_1 = StarCookie("red", 15)
print(star_cookie_1.weight)
print(star_cookie_1.color)

star_cookie_2 = StarCookie('orange', 20)
star_cookie_2.weight = 30
print(star_cookie_2.weight)
print(star_cookie_2.color) 