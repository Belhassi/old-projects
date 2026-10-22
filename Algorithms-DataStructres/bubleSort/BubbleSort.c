#include <stdio.h>

int Sort(int arr[], int size)
{
	int counter = 0;
	do
	{
		counter = 0;
		for (int i=0;i <= size;i++)
		{
			if ((arr[i] > arr[i+1]) && i < size) 
			{
				int value = arr[i];

				arr[i] = arr[i+1];
				arr[i+1] = value;

				counter += 1;
			}
		}
	} while(counter != 0);
	
	for (int i = 0; i < size; ++i)
	{
		printf("%d ", arr[i]);
	}
}

int main(int argc, char const *argv[])
{
	int array[] = {9, 8, 7, 6, 5, 4, 3, 2, 1};
	int size = sizeof(array)/sizeof(array[0]);  
	Sort(array, size);

}