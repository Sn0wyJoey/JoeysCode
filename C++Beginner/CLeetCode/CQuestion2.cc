class Solution {
public:
    string defangIPaddr(string address) {
    int x1, x2, x3, x4;

    x1 = address.find(".", 0); 
    x2 = address.find(".", x1 + 1); 
    x3 = address.find(".", x2 + 1);  
        
    string num1 = address.substr(0, x1);
    string num2 = address.substr(x1 + 1, x2 - x1 - 1);
    string num3 = address.substr(x2 + 1, x3 - x2 - 1);
    string num4 = address.substr(x3 + 1, address.size() - x3 - 1);
    
    return num1 + "[.]" + num2 + "[.]" + num3 + "[.]" + num4;
    }
};