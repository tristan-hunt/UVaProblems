using namespace std;

#include <bitset> // Compact STL for Sieve, more efficient than vector<bool>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

// Shortcuts for 'common' data types in contests
typedef long long 	ll;
typedef vector<ll> vi;
typedef pair<ll, ll> ii;
typedef vector<ii> vii;
typedef set<ll> si;
typedef map<string, ll> msi;

// Simplify repetitions/loops
#define REP(i, a, b) \
    for (int i = int(a); i < int(b); i++)
#define TRvi(c, it) \
    for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
    for(vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
    for(msi::iterator it = (c).begin(); it != (c).end(); it++)

#define INF 2000000000 //2 billion has 9 0s

ll _sieve_size; // ll is defined as: typedef long long ll
bitset<10000010> bs; // 10^7 + small extra bits - should be enough for most prime- related problems
vi primes;

void sieve(ll upperbound){ //create list of primes in [0 ... upperbound ]
    _sieve_size = upperbound + 1; //add 1 to include upperbound.
    bs.reset(); bs.flip();
    bs.set(0, false);
    bs.set(1, false);
    for (ll i=2; i<= _sieve_size; i++) if (bs.test((size_t)i)){
        // cross out multiples of i starting from i * i!
        for (ll j = i * i; j <= _sieve_size; j +=i) bs.set((size_t)j, false);
            primes.push_back((int)i); //also add this vector containing list of primes
    }
} // call this method in main method

bool isPrime(ll N){ // a good enough deterministic prime tester
    if (N < _sieve_size) return bs.test(N); // O(1) for small primes
    REP(i, 0, primes.size()-1) if (N%primes[i] == 0) return false;
    return true; // it takes longer if N is large!
} // Note - only works for N <= (last prime in vi "primes")^2 !

vi primeFactors(int N){
    vi factors; // vi "primes" (generated by sieve) is optional
    int PF_idx = 0, PF = primes[PF_idx];
    while( N != 1 && (PF * PF <= N)) { //stop at sqrt(N), but N can get smaller
        while(N % PF == 0) { N /= PF; factors.push_back(PF); } // remove this prime factor
        PF = primes[++PF_idx]; // only consider primes!
    }
    if (N != 1) factors.push_back(N); //special case if N is actually a prime.
    return factors;
}

ll eulerPhi(ll N) {
    if (N == 0){
        return 0;
    }
    if (N == 1){
        return 2; // Because we're enumerating Q, that's why!
    }
    vi factors = primeFactors(N);
    vi::iterator new_end = unique(factors.begin(), factors.end()); // get unique
    ll result = N;
    for (vi::iterator i = factors.begin(); i != new_end; i++)
        result = result - result / *i;
    return result;
}

ll sumPhis(ll N){
    ll i;
    ll sum = 0;
    for(i=1; i<N+1; i++){
        sum = sum + eulerPhi(i);
    }
    return sum;
}

ll gcd(ll a, ll b){
    if (b == 0){
        return a;
    }
    return(gcd(b, a%b));
}

void printQ(ll N){
    // Given the N enumerated rational numbers,
    // What is the rational number, Q?
    ll r = N;
    ll i = 1;
    ll eP = eulerPhi(i);
    while(r - eP > 0){ // gone too far
        r = r - eP;
        i = i + 1;
        eP = eulerPhi(i);
        //printf("%d:  r=%d - %d\n", i, r, eP);
    }
    ll denom = i;
    if (denom == 1){
        if (r == 1){
            printf("0/1\n");
            return;
        }
        printf("1/1\n");
        return;
    }


    if (isPrime(denom)){
        ll numer = r;// + eulerPhi(i); // numer is the r'th relatively prime number of denom
        printf("%llu/%llu\n", numer, denom);
        return;
    }

    else{
        i = 0; // count how many relatively prime numbers we have found
        ll numer = 0;
        //printf("Finding the %dth relatively prime number of %d\n", r, denom);
        ll j = 0; // test if j is relatively prime, increment
        while(i < r){
            j = j + 1;
            if (gcd(denom, j) == 1){ // if denom and j are relatively prime, increment i
                //printf("the %dth relatively prime number is %d\n", i, j);
                i = i + 1;
            }
        }
        numer = j; // at this point, j should hold the rth relatively prime number.
        printf("%llu/%llu\n", numer, denom);
        return;
    }
}


int main(){
    sieve(100000); //can go up to 10^7
    int rc;
    while(1){
        ll N;
        rc = scanf("%llu", &N);
        if (N == 0){
            return(0);
        }
        printQ(N);
    }
}
