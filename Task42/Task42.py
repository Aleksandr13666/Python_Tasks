# Задача 42: Узнать какая максимальная households в зоне минимального значения population.
# https://colab.research.google.com/drive/1g1SLv_VWn3z_kFEhDkB0Ik2RRBeg_lID#scrollTo=BRlhjFdImVYM

# df[df['population']==df['population'].min()]['households'].max()

# df[df['population']==df['population'].min()]['households'].agg(['max'])