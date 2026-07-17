def should_serve_customer(customer_age, on_break, time):
  is_old_enough = customer_age >= 21
  on_time = time >= 5 and time <= 10
  return is_old_enough and not on_break and on_time
