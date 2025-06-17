# IRMatcher.py
def compare_ir_signals(signal1, signal2, tolerance=0.3):
  if len(signal1) != len(signal2):
    return False

  for i in range(len(signal1)):
    a = signal1[i]
    b = signal2[i]
    if abs(a - b) > b * tolerance:
      return False

  return True
