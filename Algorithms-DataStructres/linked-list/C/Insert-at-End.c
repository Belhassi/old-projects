#include <stdio.h>
#include <stdlib.h>

struct Node {
	int Data;
	struct Node* next;
};

void Insert();
void PrintValues();

struct Node *head = NULL;

int main(int argc, char const *argv[]){
	int j;
	printf("How many numbers: ");
	scanf("%i", &j);

	for (int i = 0; i < j; ++i)
	{
		int n;
		printf("Enter number: ");
		scanf("%i", &n);
		Insert(n);
		PrintValues(head);
	}
}

void Insert(int i){
	if (head == NULL)
	{
		struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
		temp -> Data = i;
		temp -> next = NULL;

		head = temp;
	}
	else{
		struct Node *temp1 = head;
		struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
		temp -> Data = i;
		temp -> next = NULL;

		while(temp1 -> next != NULL){
			temp1 = temp1 -> next;
		}
		temp1 -> next = temp;
	}
}

void PrintValues(){
	struct Node* temp1 = head;

	while(temp1 != NULL){
		printf("%d ", temp1 -> Data);
		temp1 = temp1 -> next;
	}
}