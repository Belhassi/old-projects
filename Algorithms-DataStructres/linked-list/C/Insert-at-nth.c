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
	
	Insert(6, 1);
	PrintValues();

	Insert(1, 2);
	PrintValues();
	Insert(5, 1);
	Insert(3, 3);
	Insert(20, 4);
	PrintValues();

}

void Insert(int data, int pos){
	struct Node *temp = (struct Node*)malloc(sizeof(struct Node));	
	temp -> Data = data;
	temp -> next = NULL;

	if (pos == 1){
		temp -> next = head;
		head = temp;
		return;
	}

	struct Node *temp1 = head;
	
	for (int i = 0; i < pos-2; ++i){
		temp1 = temp1 -> next;
	}

	temp -> next = temp1;
	temp1 -> next = temp;
}

void PrintValues(){
	struct Node* temp1 = head;

	while (temp1 != NULL){
        printf("%d ", temp1->Data);
        temp1 = temp1->next;
    }
}