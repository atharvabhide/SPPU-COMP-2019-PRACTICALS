#include<bits/stdc++.h>
using namespace std;
class PersonalRecord
{
protected:
    string name;
    string address;
    string gender;
public:
    void getPersonal()
    {
        cout << "Enter the name here-\n";
        getline(cin, name);
        cout << "Enter the address here-\n";
        getline(cin, address);
        cout << "Enter the gender here-\n";
        cin >> gender;
    }
    void displayPersonal()
    {
        cout << "Name is- " << name << endl;
        cout << "Address is- " << address << endl;
        cout << "Gender is- " << gender << endl;
    }
};
class ProfessionalRecord
{
protected:
    int total_experience;
public:
    void getProfessional()
    {
        cout << "Enter the total experience in years-\n";
        cin >> total_experience;
    }
    void displayProfessional()
    {
        cout << "The total experience in years is- " << total_experience << endl;
    }
};
class AcademicRecord
{
protected:
    float ssc_marks;
    float hsc_marks;
    float graduation_marks;
public:
    void getAcademic()
    {
        cout << "Enter the ssc marks here-\n";
        cin >> ssc_marks;
        cout << "Enter the hsc marks here-\n";
        cin >> hsc_marks;
        cout << "Enter the graduation marks here-\n";
        cin >> graduation_marks;
    }
    void displayAcademic()
    {
        cout << "SSC marks are- " << ssc_marks << endl;
        cout << "HSC marks are- " << hsc_marks << endl;
        cout << "Graduation marks are- " << graduation_marks << endl;
    }
};
class Biodata : public PersonalRecord, public ProfessionalRecord, public AcademicRecord
{
public:
    void getInfo()
    {
        getPersonal();
        getProfessional();
        getAcademic();
    }
    void displayBiodata()
    {
        cout << "***************BIODATA-PERSONAL DETAILS***************\n";
        displayPersonal();
        cout << "***************BIODATA-PROFESSIONAL DETAILS***************\n";
        displayProfessional();
        cout << "***************BIODATA-ACADEMIC DETAILS***************\n";
        displayAcademic();
        cout << "***************BIODATA ENDS***************";
    }
};
int main()
{
    Biodata atharva_bhide;
    atharva_bhide.getInfo();
    atharva_bhide.displayBiodata();
    return 0;
}
