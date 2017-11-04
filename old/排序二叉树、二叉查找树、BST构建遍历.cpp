#include<iostream>
#include<vector>
using namespace std;
struct node{
	int data;
	node *left;
	node *right;
};
void insert(node* &root,int data){   /*注意此处是取root的地址！！*/ 
	if(root==NULL){
		root=new node;
		root->data=data;
		root->left=root->right=NULL;
		return ;
	}
	if(data<root->data) insert(root->left,data);
	else insert(root->right,data);
}
void preOrder(node* root,vector<int>&vi){
	if(root==NULL)  return ;
	vi.push_back(root->data);
	preOrder(root->left,vi);
	preOrder(root->right,vi);
}
void preOrderMirror(node* root,vector<int>&vi){
	if(root==NULL) return ;
	vi.push_back(root->data);
	preOrderMirror(root->right,vi);
	preOrderMirror(root->left,vi);
}
void postOrder(node* root,vector<int>&vi){
	if(root==NULL) return ;
	postOrder(root->left,vi);
	postOrder(root->right,vi);
	vi.push_back(root->data);
}
void postOrderMirror(node* root,vector<int>&vi){
	if(root==NULL) return ;
	postOrderMirror(root->right,vi);
	postOrderMirror(root->left,vi);
	vi.push_back(root->data);
}
vector<int> origin, pre, preM, post, postM;
int main(){
    int n;
    cin>>n;
    int temp;
    node* root=NULL;
	for(int i=0;i<n;i++){
        cin>>temp;
        origin.push_back(temp);
		insert(root,temp);
	}
	preOrder(root,pre);
	preOrderMirror(root,preM);
	postOrder(root,post);
	postOrderMirror(root,postM);
	if(origin==pre){
		cout<<"YES"<<endl;
		for(int i=0;i<n;i++){
			if(i<n-1)
			 cout<<post[i]<<" ";
			else
			 cout<<post[i]<<endl;
		}
	}else if(origin==preM){
		cout<<"YES"<<endl;
		for(int i=0;i<n;i++){
			if(i<n-1)
			 cout<<postM[i]<<" ";
			else
			 cout<<postM[i]<<endl;
		}
	}else{
		cout<<"NO";
	}
}





