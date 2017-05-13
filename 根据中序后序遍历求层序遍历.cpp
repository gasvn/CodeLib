#include<iostream>
#include<queue>
using namespace std;
struct node {
	int data;
	node* lchild;
	node* rchild;
};
int post[50];
int in[50];
int pre[50];
int n;
node* create(int posL, int posR, int inL, int inR) {
	if (posL > posR)
		return NULL;
	node* root = new node;
	root->data = post[posR];/*����ǰ��������ߺ���������ص��ҵ���������ֵ����ȥ�������������Ѱ���������Ӷ��ֿ�������������*/
	int k = 0;
	for (k = inL; k <= inR; k++ ) {/*���Ҷ�Ҫ���ʵ�������<=inR*/
		if (post[posR] == in[k]) {
			break;
		}
	}
	int numLeft = k - inL;
	root->lchild = create(posL, posL + numLeft - 1, inL, k - 1);/*�ؼ�ȷ���������������������ص�*/
	root->rchild = create(posL + numLeft, posR-1, k + 1, inR);/*������������������һ��ֵ�Ǹ���㣬����ע��Ҫȥ��*/
	return root;
}
void BFS(node* root) {
	int num = 0;
	queue<node*> q;
	q.push(root);
	while (!q.empty()) {
		node* now = q.front();
		q.pop();/*ȡ���ǰ��frontֵ����Ҫ�Ѷ�ǰpop��������*/
		cout << now->data;
		if (++num< n) cout << " ";/*�˴����Ƹ�ʽ�����һ�����ո�*/
		if(now->lchild!=NULL) q.push(now->lchild);
		if(now->rchild!=NULL) q.push(now->rchild);/*ע���ǵ�ǰ�ڵ�now���ӽڵ㣬��ҪŪ����*/
	}
}
int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> post[i];
	}
	for (int i = 0; i < n; i++) {
		cin >> in[i];
	}
	node* tree = create(0, n - 1, 0, n - 1);
	BFS(tree);
}
