minimize
  50 m1 + 83 m2 + 130 m3 + 61 b1 + 97 b2 + 145 b3
subject To
  2 m1 + 1.5 m2 + 3 m3 <= 10000
  1 m1 + 2 m2 + 1 m3 <= 5000
  1 m1 + 1 b1 = 3000
  1 m2 + 1 b2 = 2000
  1 m3 + 1 b3 = 900
bounds
  m1 >= 0
  m2 >= 0
  m3 >= 0
  b1 >= 0
  b2 >= 0
  b3 >= 0
generals
  m1 m2 m3 b1 b2 b3
end