def join_middle(bound_by, tag_name):
  # complete the statement below to return the string as required
  l = len(bound_by)//2
  return bound_by[0 : l] + tag_name + bound_by[ l: ]