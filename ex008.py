m = int(input('Digite um valor em metros:'.strip()))
km = m * 1000
hm = m * 100
dam = m * 10
dm = m / 10
cm = m / 100
mm = m /1000
print('''Se o valor é {}, convertendo ele:
{} km,
{} Hm,
{} Dam,
{} Dm,
{:.2f} Cm,
{:.3f} Mm.'''.format(m, km, hm, dam, dm, cm, mm))
