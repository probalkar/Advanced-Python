# zip() : This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

usernames = ['Probal', 'Awantika', 'Smita']
passwords = ('p@ssw0rd', '123456', 'qwerty')
users = dict(zip(usernames, passwords))
print(users)

# with 3 iterables
login_dates = ['2021-01-01', '2021-01-02', '2021-01-03']
users_login = zip(usernames, passwords, login_dates)
print(list(users_login))