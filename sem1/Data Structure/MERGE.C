#include<stdio.h>
#include<conio.h>
void main()
{
int a[10],b[10],c[20],i,j,k=0,m,n,o;
clrscr();
printf("Enter the size of the  first array");
scanf("%d",&n);
printf("Enter the array elements");
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
printf("Enter the size of second array");
scanf("%d",&m);
printf("Enter the elements of second array");
for(j=0;j<m;j++)
{
scanf("%d",&b[j]);
}
i=0;
j=0;
o=m+n;
for(k=0;k<o;k++)
{
if(i<n && j<m)
{
if(a[i]<b[j])
{
c[k]=a[i];
i++;
}
else{
c[k]=b[j];
j++;
}}
else if(i<n){
c[k]=a[i];
i++;
}
else
{
c[k]=b[j];
j++;
}
}
printf("The merged array is");
for(k=0;k<o;k++)
printf("%d\n",c[k]);
getch();
}
