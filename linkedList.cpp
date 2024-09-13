#include <iostream>

using namespace std;

class Node{
private:
    int prn;
    string name;
public:
    Node* next;
    Node(){
        this->prn = 0;
        this->name = "";
        this->next = nullptr;
    }
    Node(int prn,string name){
        this->prn = prn;
        this->name = name;
        this->next = nullptr;
    }
    void printInfo(){
        cout<<"PRN: "<<this->prn<<endl;
        cout<<"Name: "<<this->name<<endl;
    }
};

class LinkedList{
private:
    Node* head=nullptr;
public:
    void print(){
        Node* current = head;
        while (current != nullptr){
            current->printInfo();
            current = current->next;
        }
    }
    void printRevHelper(Node* ptr){
        if (ptr!=nullptr){
            printRevHelper(ptr->next);
            ptr->printInfo();
        }
    }
    void printRev(){
        if (head!=nullptr){
            Node* current = head;
            printRevHelper(head);
        }
    }
    void makePresident(int prn,string name){
        Node* elem = new Node(prn,name);
        if (head == nullptr){
            head = elem;
        }
        else{
            elem->next = head;
            head = elem;
        }
    }
    void makeSecretary(int prn,string name){
        if (head==nullptr){
            Node* current = head;
            Node* elem = new Node(prn,name);
            head = elem;
        }
        else{
            Node* current = head;
            while (current->next != nullptr){
                current = current->next;
            }
            Node* elem = new Node(prn,name);
            current->next = elem;
        }
    }
    void addMember(int prn,string name){
        Node* elem = new Node(prn,name);
        if (head==nullptr){
            Node* current = head;
            head = elem;
        }
        elem->next = head->next;
        head->next = elem;
    }
    void deleteMember(int index){
        int i=0;
        Node* prev = head;
        if (head==nullptr){
            cout<<"Nothing to delete"<<endl;
        }
        else{
            while (i+1<index && prev!=nullptr){
                prev = prev->next;
                i++;
            }
            if (i+1<index){
                char c;
                cout<<"Index is greater than last index"<<endl;
                cout<<"Would you like to delete last element: (y/n)"<<endl;
                cin>>c;
                if (c=='y'){
                    delete prev->next;
                    prev->next = nullptr;
                }
            }
            else{
                Node* current = prev->next;
                prev->next = current->next;
                delete current;
            }
        }
    }
};

int main(){
    LinkedList l1;
    l1.makePresident(1,"President");
    l1.makeSecretary(2,"Secretary");
    l1.addMember(3,"Member1");
    l1.addMember(4,"Member2");
    l1.addMember(5,"Member3");
    l1.deleteMember(3);
    cout<<"Printing"<<endl;
    l1.print();
    cout<<"Printing in reverse"<<endl;
    l1.printRev();
}