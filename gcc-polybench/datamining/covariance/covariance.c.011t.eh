
;; Function init_array (init_array, funcdef_no=6, decl_uid=4680, cgraph_uid=7, symbol_order=6)

init_array (int m, int n, double * float_n, double[1200] * data)
{
  int j;
  int i;

  _1 = (double) n;
  *float_n = _1;
  i = 0;
  goto <D.4688>;
  <D.4687>:
  j = 0;
  goto <D.4685>;
  <D.4684>:
  _2 = (double) i;
  _3 = (double) j;
  _4 = _2 * _3;
  _5 = (long unsigned int) i;
  _6 = _5 * 9600;
  _7 = data + _6;
  _8 = _4 / 1.2e+3;
  *_7[j] = _8;
  j = j + 1;
  <D.4685>:
  if (j <= 1199) goto <D.4684>; else goto <D.4686>;
  <D.4686>:
  i = i + 1;
  <D.4688>:
  if (i <= 1399) goto <D.4687>; else goto <D.4689>;
  <D.4689>:
  return;
}



;; Function print_array (print_array, funcdef_no=7, decl_uid=4692, cgraph_uid=8, symbol_order=7)

print_array (int m, double[1200] * cov)
{
  int j;
  int i;

  stderr.0_1 = stderr;
  __builtin_fwrite ("==BEGIN DUMP_ARRAYS==\n", 1, 22, stderr.0_1);
  stderr.1_2 = stderr;
  fprintf (stderr.1_2, "begin dump: %s", "cov");
  i = 0;
  goto <D.4700>;
  <D.4699>:
  j = 0;
  goto <D.4697>;
  <D.4696>:
  _3 = i * m;
  _4 = j + _3;
  _5 = _4 % 20;
  if (_5 == 0) goto <D.4745>; else goto <D.4746>;
  <D.4745>:
  stderr.2_6 = stderr;
  __builtin_fputc (10, stderr.2_6);
  <D.4746>:
  _7 = (long unsigned int) i;
  _8 = _7 * 9600;
  _9 = cov + _8;
  _10 = *_9[j];
  stderr.3_11 = stderr;
  fprintf (stderr.3_11, "%0.2lf ", _10);
  j = j + 1;
  <D.4697>:
  if (j < m) goto <D.4696>; else goto <D.4698>;
  <D.4698>:
  i = i + 1;
  <D.4700>:
  if (i < m) goto <D.4699>; else goto <D.4701>;
  <D.4701>:
  stderr.4_12 = stderr;
  fprintf (stderr.4_12, "\nend   dump: %s\n", "cov");
  stderr.5_13 = stderr;
  __builtin_fwrite ("==END   DUMP_ARRAYS==\n", 1, 22, stderr.5_13);
  return;
}



;; Function kernel_covariance (kernel_covariance, funcdef_no=8, decl_uid=4708, cgraph_uid=9, symbol_order=8)

kernel_covariance (int m, int n, double float_n, double[1200] * data, double[1200] * cov, double * mean)
{
  int k;
  int j;
  int i;

  j = 0;
  goto <D.4717>;
  <D.4716>:
  _1 = (long unsigned int) j;
  _2 = _1 * 8;
  _3 = mean + _2;
  *_3 = 0.0;
  i = 0;
  goto <D.4714>;
  <D.4713>:
  _4 = (long unsigned int) j;
  _5 = _4 * 8;
  _6 = mean + _5;
  _7 = *_6;
  _8 = (long unsigned int) i;
  _9 = _8 * 9600;
  _10 = data + _9;
  _11 = *_10[j];
  _12 = (long unsigned int) j;
  _13 = _12 * 8;
  _14 = mean + _13;
  _15 = _7 + _11;
  *_14 = _15;
  i = i + 1;
  <D.4714>:
  if (i < n) goto <D.4713>; else goto <D.4715>;
  <D.4715>:
  _16 = (long unsigned int) j;
  _17 = _16 * 8;
  _18 = mean + _17;
  _19 = *_18;
  _20 = (long unsigned int) j;
  _21 = _20 * 8;
  _22 = mean + _21;
  _23 = _19 / float_n;
  *_22 = _23;
  j = j + 1;
  <D.4717>:
  if (j < m) goto <D.4716>; else goto <D.4718>;
  <D.4718>:
  i = 0;
  goto <D.4723>;
  <D.4722>:
  j = 0;
  goto <D.4720>;
  <D.4719>:
  _24 = (long unsigned int) i;
  _25 = _24 * 9600;
  _26 = data + _25;
  _27 = *_26[j];
  _28 = (long unsigned int) j;
  _29 = _28 * 8;
  _30 = mean + _29;
  _31 = *_30;
  _32 = (long unsigned int) i;
  _33 = _32 * 9600;
  _34 = data + _33;
  _35 = _27 - _31;
  *_34[j] = _35;
  j = j + 1;
  <D.4720>:
  if (j < m) goto <D.4719>; else goto <D.4721>;
  <D.4721>:
  i = i + 1;
  <D.4723>:
  if (i < n) goto <D.4722>; else goto <D.4724>;
  <D.4724>:
  i = 0;
  goto <D.4732>;
  <D.4731>:
  j = i;
  goto <D.4729>;
  <D.4728>:
  _36 = (long unsigned int) i;
  _37 = _36 * 9600;
  _38 = cov + _37;
  *_38[j] = 0.0;
  k = 0;
  goto <D.4726>;
  <D.4725>:
  _39 = (long unsigned int) i;
  _40 = _39 * 9600;
  _41 = cov + _40;
  _42 = *_41[j];
  _43 = (long unsigned int) k;
  _44 = _43 * 9600;
  _45 = data + _44;
  _46 = *_45[i];
  _47 = (long unsigned int) k;
  _48 = _47 * 9600;
  _49 = data + _48;
  _50 = *_49[j];
  _51 = _46 * _50;
  _52 = (long unsigned int) i;
  _53 = _52 * 9600;
  _54 = cov + _53;
  _55 = _42 + _51;
  *_54[j] = _55;
  k = k + 1;
  <D.4726>:
  if (k < n) goto <D.4725>; else goto <D.4727>;
  <D.4727>:
  _56 = (long unsigned int) i;
  _57 = _56 * 9600;
  _58 = cov + _57;
  _59 = *_58[j];
  _60 = float_n - 1.0e+0;
  _61 = (long unsigned int) i;
  _62 = _61 * 9600;
  _63 = cov + _62;
  _64 = _59 / _60;
  *_63[j] = _64;
  _65 = (long unsigned int) i;
  _66 = _65 * 9600;
  _67 = cov + _66;
  _68 = (long unsigned int) j;
  _69 = _68 * 9600;
  _70 = cov + _69;
  _71 = *_67[j];
  *_70[i] = _71;
  j = j + 1;
  <D.4729>:
  if (j < m) goto <D.4728>; else goto <D.4730>;
  <D.4730>:
  i = i + 1;
  <D.4732>:
  if (i < m) goto <D.4731>; else goto <D.4733>;
  <D.4733>:
  return;
}



;; Function main (main, funcdef_no=9, decl_uid=4736, cgraph_uid=10, symbol_order=9)

main (int argc, char * * argv)
{
  const unsigned char D.4752;
  double[1200] * mean;
  double[1200][1200] * cov;
  double[1400][1200] * data;
  double float_n;
  int m;
  int n;
  int D.4751;

  n = 1400;
  m = 1200;
  data = polybench_alloc_data (1680000, 8);
  cov = polybench_alloc_data (1440000, 8);
  mean = polybench_alloc_data (1200, 8);
  init_array (m, n, &float_n, data);
  float_n.6_1 = float_n;
  kernel_covariance (m, n, float_n.6_1, data, cov, mean);
  if (argc > 42) goto <D.4747>; else goto <D.4748>;
  <D.4747>:
  _2 = *argv;
  D.4752 = MEM[(const unsigned char * {ref-all})_2];
  _3 = (int) D.4752;
  if (_3 == 0) goto <D.4749>; else goto <D.4750>;
  <D.4749>:
  print_array (m, cov);
  <D.4750>:
  <D.4748>:
  free (data);
  free (cov);
  free (mean);
  D.4751 = 0;
  goto <D.4754>;
  <D.4754>:
  float_n = {CLOBBER};
  goto <D.4753>;
  D.4751 = 0;
  goto <D.4753>;
  <D.4753>:
  return D.4751;
}


