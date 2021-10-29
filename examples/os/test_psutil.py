import psutil, os

p = psutil.Process(os.getpid())
p.nice()

# Unix:
p.nice(32)

# Windows:
p.nice(psutil.IDLE_PRIORITY_CLASS)
# p.nice(psutil.REALTIME_PRIORITY_CLASS) -> 256
# p.nice(psutil.HIGH_PRIORITY_CLASS) -> 128
# p.nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS) ->32768
# p.nice(psutil.NORMAL_PRIORITY_CLASS) -> 32
# p.nice(psutil.IDLE_PRIORITY_CLASS) -> 64
# p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS) -> 16384
