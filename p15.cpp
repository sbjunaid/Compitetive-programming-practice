#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, q;
        cin >> n >> q;
        vector<int> a(n);
        vector<int> x(q);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        for (int i = 0; i < q; i++) {
            cin >> x[i];
        }
        for (int i = 0; i < q; i++) {
            for (int j = 0; j < n; j++) {
                if (a[j] % (1 << x[i]) == 0) {
                    a[j] += 1 << (x[i] - 1);
                }
            }
        }
        for (int i = 0; i < n; i++) {
            cout << a[i] << " ";
        }
        cout << endl;
    }
    return 0;
}
