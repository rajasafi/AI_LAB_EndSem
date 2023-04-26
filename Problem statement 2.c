// Raja safi
// 202051151
// AI visionaries

#include<bits/stdc++.h>

using namespace std;

// 0 - 1
class Random {
	vector<double> randoms;
	public:
	Random() {
        srand(time(0));
        srand((unsigned)time(NULL));
        for(int i = 0; i < 10000000; i++) 
            randoms.push_back((double)rand()/RAND_MAX), randoms.back();
    }
	vector<double> getRandoms() {
		return randoms;
	}
	
};

class Data {
    int CovidBeds = 1000, NormalBeds = 1000, itr = 0;
    vector<string> ageGrps = {"0-18", "18-40", "40-65","65+"};
    
    unordered_map<string, int> Population;
    vector<double> percentHospitalized = {0.5, 1, 2, 10};
public:
    vector<double> randoms;
    Data() {
        Random obj;
        randoms = obj.getRandoms();

        for(auto it: ageGrps) 
            Population[it] = randoms[itr++] * 50000;
        
    }

    void PopulationNextWeek() {
        for(auto it: ageGrps) 
            Population[it] += randoms[itr++] * 2000 - 1000;
    }

    vector<int> numPatients() {
        vector<int> patients;
        for(int i = 0; i < ageGrps.size(); i++) {
            int num = Population[ageGrps[i]] * percentHospitalized[i] / 100;
            patients.push_back(num > 0 ? num : 0);
        }
        return patients;
    }

    pair<int, int> 

};

class Driver {
public:
    void run() {
        int itr = 0;
        Data obj;
        double avg;
        for(int i = 0; i < 1000000; i++) {
            
            vector<int> patients = obj.numPatients();
            for(auto it: patients) 
                avg = (avg * itr) + it / (itr + 1);
            obj.PopulationNextWeek();
        }
        cout << avg << " ";
    }
};

int main() {
    Driver obj;
    obj.run();
    return 0;
}