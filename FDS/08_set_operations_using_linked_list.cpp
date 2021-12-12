#include <bits/stdc++.h>

using namespace std;

class node
{
    public:
        int rollno;
        node *next;
		node(int num) //constructor
		{
			rollno = num;
			next = NULL;
		}
}*all_head = NULL, *vanilla_head = NULL, *butter_head = NULL, *union_head = NULL, *inters_head = NULL, *diff_head = NULL;


void append(node **head_ref)  //insert at end
{
	int num;

	cout<<"Enter Rollno: ";
	cin>>num;

	node *new_node = new node(num);

	if (*head_ref == NULL)  //if list is empty
	{
		*head_ref = new_node;
		return;
	}

	node *last = *head_ref;
	while (last -> next != NULL)
	{
		last = last -> next;
	}

	last -> next = new_node;
}

void append(node **head_ref, int key)
{
	node *new_node = new node(key);

	if (*head_ref == NULL)  //if list is empty
	{
		*head_ref = new_node;
		return;
	}

	node *last = *head_ref;
	while (last -> next != NULL)
	{
		last = last -> next;
	}

	last -> next = new_node;
}

void display_list(node **head_ref)
{
	cout<<"\n";
	node *temp = *head_ref;

	if (temp == NULL)
	{
		cout<<"List is empty";
		return;
	}
	while (temp != NULL)
	{
		cout<<temp -> rollno<<" ";
		temp = temp -> next;
	}
    cout<<"\n";
}

void get_all()
{
    int count;
    cout<<"\nEnter total students: ";
    cin>>count;
    
    for (int i = 0; i < count; i++)
    {
        append(&all_head);
    }

    cout<<"\nAll students: ";
    display_list(&all_head);
}

void get_vanilla()
{
    int count;
    cout<<"\nEnter total students who like vanilla: ";
    cin>>count;
    
    for (int i = 0; i < count; i++)
    {
        append(&vanilla_head);
    }

    cout<<"\nStudents who like vanilla: ";
    display_list(&vanilla_head);
}

void get_butter()
{
    int count;
    cout<<"\nEnter total students who like butterscotch: ";
    cin>>count;
    
    for (int i = 0; i < count; i++)
    {
        append(&butter_head);
    }

    cout<<"\nStudents who like butterscotch: ";
    display_list(&butter_head);
}

node **unio(node **head1, node **head2)
{
    //fill union list with all elements of list 1
    node *temp1 = *head1;
    while (temp1 != NULL)
    {
        append(&union_head, (temp1 -> rollno));
        temp1 = temp1 -> next;
    }

    //fill union list with non-common elements from list 2
    node *temp2 = *head2;
    while (temp2 != NULL)
    {
        temp1 = *head1;
        bool flag = false;
        while (temp1 != NULL)
        {
            if ((temp2 -> rollno) == (temp1 -> rollno))
                flag = true;
            temp1 = temp1 -> next;
        }

        if (!flag)
        {
            append(&union_head, (temp2 -> rollno));
        }

        temp2 = temp2 -> next;
    }

    return &union_head;
}

node **inters(node **head1, node **head2)
{
    node *temp1 = *head1;
    while (temp1 != NULL)
    {
        node *temp2 = *head2;
        while (temp2 != NULL)
        {
            if ((temp1 -> rollno) == (temp2 -> rollno))
            {
                append(&inters_head, (temp1 -> rollno));
            }

            temp2 = temp2 -> next;
        }

        temp1 = temp1 -> next;
    }

    return &inters_head;
}

node **diff(node **head1, node **head2)
{
    node *temp1 = *head1;
    while (temp1 != NULL)
    {
        node *temp2 = *head2;
        bool flag = false;
        while (temp2 != NULL)
        {
            if ((temp1 -> rollno) == (temp2 -> rollno))
            {
                flag = true;
            }
            temp2 = temp2 -> next;
        }

        if(!flag)
        {
            append(&diff_head, (temp1 -> rollno));
        }
        temp1 = temp1 -> next;
    }

    return &diff_head;
}

int main()
{
    bool exit = false;
    int choice;

    do
    {
        cout<<"\n1. To enter data";
        cout<<"\n2. To display the rollnos of students who like vanila or butterscotch";
        cout<<"\n3. To display the rollnos of students who like only vanila";
        cout<<"\n4. To display the rollnos of students who like only butterscotch";
        cout<<"\n5. To display the rollnos of students who like both vanila and butterscotch ";
        cout<<"\n6. To display the rollnos of students who neither like vanila nor butterscotch";
        cout<<"\n7. Exit";
        cout<<"\nEnter choice: ";
        cin>>choice;
        
        switch (choice)
        {
            case 1:
                get_all();
                get_vanilla();
                get_butter();
                break;
            
            case 2:
                cout<<"Students who like vanilla or butterscotch: ";
                display_list( unio(&vanilla_head, &butter_head) );
                break;
            
            case 3:
                cout<<"Students who like only vanilla: ";
                display_list(&vanilla_head);
                break;

            case 4:
                cout<<"Students who like butterscotch: ";
                display_list(&butter_head);
                break;
            
            case 5:
                cout<<"Students who like both vanilla and butterscotch: ";
                display_list( inters(&vanilla_head, &butter_head) );
                break;
            
            case 6:
                cout<<"Students who like neither vanilla nor butterscotch: ";
                display_list( diff(&all_head, unio(&vanilla_head, &butter_head)) );
                break;
            
            case 7:
                exit = true;
                break;
        }
    } while (!exit);
    
}
