#include<stdio.h>

int main()
{
	int test, m, n, dis, array[100][100];

	scanf("%d", &test);

	for (int i = 0; i < test; i++) //test 개수만큼
	{
		scanf("%d %d", &m, &n);
		dis = 0; 

		for (int j=0; j < m; j++) //m행 탐색
			for (int k=0; k < n; k++)//n열 탐색
				scanf("%d", &array[j][k]);
			
			for (int k = 0; k < n; k++) //모든 열 횟수 초기화
			{
				int cnt = 0;
				for (int j = m - 1; j >= 0; j--)//아랫쪽 행부터 탐색
				{
					if (array[j][k] == 1)
						dis += (m - j) - (++cnt);
				}
			}
			
		printf("%d\n", dis);
		
	}
	return 0;

}