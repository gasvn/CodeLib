#include<iostream>
using namespace std;
struct node {
	int data;
	node* lchild;
	node* rchild;
};
node* newNode(int v) {
	node* Node = new node;
	Node->data = v;
	Node->lchild = Node->rchild = NULL;
	return Node;
}
void insert(node* &root, int x) {
	if (root == NULL) {
		root = newNode(x);
		return;
	}
	if(root->lchild)
}
node* Create(int data[], int n) {
	node* root = NULL;//´´½¨Ê÷¸ù
	for (int i = 0; i < n; i++) {
		insert(root, data[i]);
	}
	return root;
}
int main() {
	
}