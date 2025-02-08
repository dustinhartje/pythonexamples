# https://progressbar-2.readthedocs.io/en/latest/examples.html
# Docs can be difficult to parse though, googling may be needed for advanced
# Below are specific examples I've worked out in my various scripts


import progressbar
import time

LOOPS = 50

# Simple progressbar
progress = 0

widgets = [progressbar.Percentage(),
           progressbar.Bar(),
           ]
bar = progressbar.ProgressBar(widgets=widgets,
                              max_value=LOOPS).start()
while progress < LOOPS:
    progress += 1
    bar.update(progress)
    time.sleep(0.1)
bar.finish()


# More advanced with time elapsed and remaining
progress = 0

bar_label = (f"%(value)d of {LOOPS} naps completed in "
             "%(elapsed)s ")
eta_widget = progressbar.ETA(format_not_started='--:--:--',
                             format_finished='Time: %(elapsed)8s',
                             format='Remaining: %(eta)8s',
                             format_zero='Remaining: 00:00:00',
                             format_na='Remaining: N/A',
                             )
widgets = [progressbar.Percentage(),
           progressbar.Bar(),
           progressbar.FormatLabel(bar_label),
           eta_widget,
           ]
bar = progressbar.ProgressBar(widgets=widgets,
                              max_value=LOOPS).start()
while progress < LOOPS:
    progress += 1
    bar.update(progress)
    time.sleep(0.1)
bar.finish()
