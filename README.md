# backend

Link to database design: https://drive.google.com/file/d/1BxUF6cSr11s3BiKVhRrI3o_O1tWd-P0E/view?usp=sharing
Note that you can comment there so feel free to do it.


Weapon Customization Validation
Decided to save the vaidations in code over in DB because:
* Fast implementation.
* Static options. (No more customizations will be added for this assignment).
* Performance. (Because it is already in the code we don't need to fetch the data from DB).

In case of prudction product I would suggest saving the validation for weapons and customization in the DB 
for more flexible approach. To do it we will use a junction table because it will be a many to many relationship.
