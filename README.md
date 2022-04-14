# Accuid-Project_csv-to-boxplots
The main purpose of this project is to automate visualization of exported CSV files. Each CSV contains file format below,

RanN(Random # generated),	Sample1,	Sample2,	BloodR(Blood relationship),	N(# of genetic marker used for comparison),	PC(Parent-Child),	FS(Full Sibling),
HS(Half Sibling),	FC(First Cousin),	SC(Second Cousin)

The example value of each column: 
1,	K21_46_01,	re_K21_46_02,	P_C,	587,	5.66E+41,	1.76E+26,	3.57E+24,	3.42E+13,	4796.274653
*29999 more columns

Aim
The goal was to find the trend among exported Likelyhood Ratio(LR) value of genetic markers in each blood relationships, and setup a evaluation standard to distinguish between each other.

Approach
Applied Pandas to read each CSV files, Numpy to log-scale P-values, and seaborn,pyplot to generate and visualize boxplot.
Outliers were neglected due to the extortion of plots. (Q3+1.5IQR>,Q1-1.5IQR<)

Results
Boxplots representing each columns(PC,FS,HS,FC,SC)

![Indep](https://user-images.githubusercontent.com/101860126/163285420-69751330-ebb0-47fc-b126-a5742e8d8b16.png)
