#include<stdio.h>
#include<limits.h>
#include<stdlib.h>
#include<string.h>

#define vectorlenght 8192
#define vectormask 8
#define totalvector 2048
#define intlength 32
#define no_category 5

void init(FILE *);
void display_home(FILE *);
void category_home(FILE *);
void user_home(FILE *);
void add_user(FILE *);
void list_user(FILE *fp);
void updateUsers(FILE *fp, long int pos);
int totalINODES = 0;
void getDetails(FILE *, int);

struct usermeta
{
	int index;
	int free;
	long int direct[20];
	long int indirect;
};
struct categorymeta
{
	int free;
	long int direct[20];
	long int indirect;
};
struct user
{
	char name[10];
	long int cat[5];
};
struct categories
{
	char name[10];
	long int offset;
};

struct bitV
{
	unsigned int A : 1;
	unsigned int B : 1;
	unsigned int C : 1;
	unsigned int D : 1;
	unsigned int E : 1;
	unsigned int F : 1;
	unsigned int G : 1;
	unsigned int H : 1;
	unsigned int I : 1;
	unsigned int J : 1;
	unsigned int K : 1;
	unsigned int L : 1;
	unsigned int M : 1;
	unsigned int N : 1;
	unsigned int O : 1;
	unsigned int P : 1;
	unsigned int Q : 1;
	unsigned int R : 1;
	unsigned int S : 1;
	unsigned int T : 1;
	unsigned int U : 1;
	unsigned int V : 1;
	unsigned int W : 1;
	unsigned int X : 1;
	unsigned int Y : 1;
	unsigned int Z : 1;
	unsigned int a : 1;
	unsigned int b : 1;
	unsigned int c : 1;
	unsigned int d : 1;
	unsigned int e : 1;
	unsigned int f : 1;

};

void main()
{
	FILE *fp;
	fp = fopen("test.bin", "rb+");

	if (fp == NULL)
	{
		printf("File not exists\n");
	}

	else
	{
		struct bitV vector;
		int n = 0;
		fread(&vector, sizeof(struct bitV), 1, fp);
		if (!(vector.A))
		{
			fseek(fp, 0, SEEK_SET);
			init(fp);
		}
		display_home(fp);
	}
	fclose(fp);
}

void init(FILE *fp)
{

	int i = 0,j=0;
	struct bitV vector;
	while (i < 2)
	{
		j = 0;
		memset(&vector, 0, sizeof(vector));
		while (j < 32)
		{
			setValue(&vector, j+1);
			j++;
		}
		fwrite(&vector, sizeof(struct bitV), 1, fp);
		i++;
	}
	memset(&vector, 0, sizeof(vector));
	vector.A = 1;
	vector.B = 1;
	fwrite(&vector, sizeof(vector), 1, fp);
}

void display_home(FILE *fp)
{
	int choice;
	do
	{
		printf("1:users\n2:category\n3:exit\n");
		scanf("%d", &choice);
		switch (choice)
		{
		case 1:
			user_home(fp);
			break;
		case 2:
			category_home(fp);
			break;
		case 3:
			exit(1);
		default:
			printf("enter the correct value\n");
		}
	} while (choice != 3);
}

void category_home(FILE *fp)
{
	
}

void user_home(FILE *fp)
{

	int choice=0,id=0;
	do
	{
		printf("\n1:add user\n2:list_user\n3:goback\n");
		scanf("%d", &choice);
		switch (choice)
		{
			case 1:
				add_user(fp);
				break;
			case 2:
				printf("userid\tusername\n");
				list_user(fp);
				printf("Enter userid\n");
				scanf("%d", &id);
				getDetails(fp,id);
				break;
			case 3:
				exit(1);
				break;
			default:
				printf("enter the correct value\n");
		}
	} while (choice != -1);
	fclose(fp);
}

void getDetails(FILE *fp,int id)
{
	fseek(fp, vectorlenght, SEEK_SET);
	int index = 0, position = 0, i = 0, tell = 0;
	struct usermeta users;
	struct user test;
	index = id / 20;
	position = id % 20;
	memset(&users, 0, sizeof(users));
	fread(&users, sizeof(users), 1, fp);
	while (i != index)
	{
		tell = users.indirect;
		fseek(fp, tell, SEEK_SET);
		fread(&users, sizeof(users), 1, fp);
		i++;
	}
	tell = users.direct[position];
	fseek(fp, tell, SEEK_SET);
	memset(&test, 0, sizeof(test));
	fread(&test, sizeof(test), 1, fp);
	printf("%s", test.name);
}

void add_user(FILE *fp)
{
	printf("Enter username");
	struct user test;
	memset(&test, 0, sizeof(test));
	scanf("%s", test.name);
	int free = getfreespace(fp, 1);
	free = free * 128;
	printf("stored at:%d\n", free);
	fseek(fp, free, SEEK_SET);
	for (int i = 0; i < no_category; i++)
	{
		test.cat[i] = -1;
	}
	fwrite(&test, sizeof(struct user), 1, fp);
	fseek(fp, free, SEEK_SET);
	updateUsers(fp, ftell(fp));
}

void updateUsers(FILE *fp, long int pos)
{
	fseek(fp, vectorlenght, SEEK_SET);
	//printf("%ld", ftell(fp));
	struct usermeta users;
	int i = 0;
	memset(&users, 0, sizeof(users));
	fread(&users, sizeof(users), 1, fp);
	int index = users.index;
	int tell=0,temp=0;
	while (i!=index)
	{
		tell = users.indirect;
		fseek(fp, tell, SEEK_SET);
		fread(&users, sizeof(users), 1, fp);
		i++;
	}
	if (users.free == 20)
	{
		i++;
		int free=getfreespace(fp, 1);
		free = free * 128;
		
		users.indirect = free;
		fseek(fp, -sizeof(users), SEEK_CUR);
		printf("20 :%ld", ftell(fp));
		fwrite(&users, sizeof(users), 1, fp);
		memset(&users, 0, sizeof(users));
		
		fseek(fp, vectorlenght, SEEK_SET);
		fread(&users, sizeof(users), 1, fp);
		users.index = users.index + 1;
		fseek(fp, -sizeof(users), SEEK_CUR);
		fwrite(&users, sizeof(users), 1, fp);
		
		
		memset(&users, 0, sizeof(users));
		fseek(fp, free, SEEK_SET);
		printf("%d", free);
		users.free = 0;
		users.direct[users.free] = free;
		temp=users.free = users.free + 1;
		fwrite(&users, sizeof(users), 1, fp);
		
	}
	else
	{
		printf("taken: %ld\n", pos);
		users.direct[users.free] = pos;
		fseek(fp, -sizeof(users), SEEK_CUR);
		temp=users.free = users.free + 1; 
		fwrite(&users, sizeof(users), 1, fp);
	}
	printf("your id is %d", ((i * 20) + (temp - 1)));
}

void list_user(FILE *fp)
{
	int tell = ftell(fp);
	int i = 0, j = 0, free;;
	struct usermeta users;
	struct user test;
	memset(&users, 0, sizeof(users));
	fseek(fp, vectorlenght, SEEK_SET);
	fread(&users, sizeof(users), 1, fp);
	int index = users.index;
	fseek(fp, vectorlenght, SEEK_SET);
	int count = 0;
	while (i<=index)
	{
		memset(&users, 0, sizeof(users));
		fread(&users, sizeof(users), 1, fp);
		free = users.free;
		j = 0;
		while (j < free)
		{
			memset(&test, 0, sizeof(test));
			fseek(fp, users.direct[j], SEEK_SET);
			fread(&test, sizeof(test), 1, fp);
			printf("%d-->\t%s\n",count, test.name);
			count++;
			j++;
		}
		if (index > 0)
		{
			fseek(fp, users.indirect, SEEK_SET);
		}
		i++;
	}
	fseek(fp, tell, SEEK_SET);
	
}

int getfreespace(FILE *fp, int flag)
{
	int tell = ftell(fp);
	int i = 2;
	int j = 0;
	fseek(fp, vectormask, SEEK_SET);
	struct bitV vector;
	while (i < (totalvector))
	{
		j = 0;
		memset(&vector, 0, sizeof(vector));
		fread(&vector, sizeof(vector), 1, fp);
		while (j < intlength)
		{
			if (getValue(j+1,vector) == 0)
			{
				if (flag)
				{
					setValue(&vector, j+1);
					fseek(fp, -sizeof(vector), SEEK_CUR);
					fwrite(&vector, sizeof(vector), 1, fp);
				}
				fseek(fp, tell, SEEK_SET);
				return ((i) * 32) + j;
			}
			j++;
		}
		i++;
	}
}

int setValue(struct bitV *vector, int i)
{
	switch (i)
	{
	case 1:
		return (*vector).A = 1;
	case 2:
		return (*vector).B = 1;
	case 3:
		return (*vector).C = 1;
	case 4:
		return (*vector).D = 1;
	case 5:
		return (*vector).E = 1;
	case 6:
		return (*vector).F = 1;
	case 7:
		return (*vector).G = 1;
	case 8:
		return (*vector).H = 1;
	case 9:
		return (*vector).I = 1;
	case 10:
		return (*vector).J = 1;
	case 11:
		return (*vector).K = 1;
	case 12:
		return (*vector).L = 1;
	case 13:
		return (*vector).M = 1;
	case 14:
		return (*vector).N = 1;
	case 15:
		return (*vector).O = 1;
	case 16:
		return (*vector).P = 1;
	case 17:
		return (*vector).Q = 1;
	case 18:
		return (*vector).R = 1;
	case 19:
		return (*vector).S = 1;
	case 20:
		return (*vector).T = 1;
	case 21:
		return (*vector).U = 1;
	case 22:
		return (*vector).V = 1;
	case 23:
		return (*vector).W = 1;
	case 24:
		return (*vector).X = 1;
	case 25:
		return (*vector).Y = 1;
	case 26:
		return (*vector).Z = 1;
	case 27:
		return (*vector).a = 1;
	case 28:
		return (*vector).b = 1;
	case 29:
		return (*vector).c = 1;
	case 30:
		return (*vector).d = 1;
	case 31:
		return (*vector).e = 1;
	case 32:
		return (*vector).f = 1;
	}
}

int getValue(int i, struct bitV vector)
{
	switch (i)
	{
	case 1:
		return vector.A;
	case 2:
		return vector.B;
	case 3:
		return vector.C;
	case 4:
		return vector.D;
	case 5:
		return vector.E;
	case 6:
		return vector.F;
	case 7:
		return vector.G;
	case 8:
		return vector.H;
	case 9:
		return vector.I;
	case 10:
		return vector.J;
	case 11:
		return vector.K;
	case 12:
		return vector.L;
	case 13:
		return vector.M;
	case 14:
		return vector.N;
	case 15:
		return vector.O;
	case 16:
		return vector.P;
	case 17:
		return vector.Q;
	case 18:
		return vector.R;
	case 19:
		return vector.S;
	case 20:
		return vector.T;
	case 21:
		return vector.U;
	case 22:
		return vector.V;
	case 23:
		return vector.W;
	case 24:
		return vector.X;
	case 25:
		return vector.Y;
	case 26:
		return vector.Z;
	case 27:
		return vector.a;
	case 28:
		return vector.b;
	case 29:
		return vector.c;
	case 30:
		return vector.d;
	case 31:
		return vector.e;
	case 32:
		return vector.f;
	}
}