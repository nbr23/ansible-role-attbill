ansible-role-attbill
=========

Simple role to retrieve your monthly AT&T bills.

Role Variables
--------------

- `att_phone_number`: Phone number of the account to retrieve the bill for
- `att_password`: Password of the account
- `att_bill_path`: Output path for the bill
- `att_bill_date`: date for which to get monthly bill from. The default value
  will get the bill for the previous month.


Example Playbook
----------------

```
---
- hosts: all
  gather_facts: true
  become: false

  roles:
    - {
      role: ansible-role-attbill,
      att_bill_path: /tmp/attbill.pdf,
      att_phone_number: 5550100,
      att_password: 'password',
      att_bill_date: '{{ ansible_date_time.date | format_date | previous_month }}',
    }
```

License
-------

MIT
