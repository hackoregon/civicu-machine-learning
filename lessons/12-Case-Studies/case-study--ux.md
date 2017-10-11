# User Experience (UX) Design

Can Machine Learning help with UX Design decisions?

- Do you have data about user experience?
- Can you come up with a measure of success and what it will look like in your data?

Let's look at some best practices at large online booking systems for vacation rentals.

## Online Housing Booking

- [Hilton](hilton.com)
- [Home Away](homeaway.com)
- [FlipKey](flipkey.com)

## 3 Problems

### Problem 1: Predict Request Acceptance Rate

What is the likelihood of a host accepting a customer's booking request?

A reservation system often involves some back and forth between hosts and guests to arrange a booking.

- Can I bring my 5 dogs?
- Did you know there's a concert in the park that weekend?
- How big is the refrigerator?
- What is the parking situation?

This interaction is stored in a timeline or log file associated with each reservation attempt.

First, what kind of data wil you look for in the databases at your company?
How is it likely to be stored and what would be a good way to denormalize it to create your feature (factor) table `X`?
What is your success criteria?
What query on your database is likely to give you your success criteria?
What features might you need to generate or transform to make them useful for prediction?

### Problem 2: A/B Testing of Forced Minimum Request Message Length

Treatment group is "required" to write a message with a minimu of 240 characters.

Will message content/meaning be changed?
Will acceptance rate be improved?
Will host experience be improved?
Will grammar/spelling be improved?
Will professionalism be improved or degraded?

### Problem 3: A/B Testing of Forced Replay within 12 Hours

How is host UX affected?
How is guest UX affected?
How is acceptance rate affected

## The Data

TODO: example database schema

TODO: example table of features (leave some good generated features out)

### Example Features

- type of interaction (phone call, direct email/SMS, support email/chat/SMS, direct chat through platform, platform page visit/search)
- reservation ID
- guest ID, name, profile details
- host ID, name, profile details
- room ID, details
- property ID, details
- asks for additional requirement types (pets, cleaning, early checkin, warm up the hottub, etc)
- datetime of request
- datetime of host reply
- number of guests
- number of interactions
- terms of service accepted
- terms of service replied to
- inquiry datetime (is weekday/weekend)
- datetime of reservation (includes a weekend, includes a holiday)
- site capacity, and requested num guests (num_guests / site_capacity)
- checkin/checkout day (whether it's a holliday, high demand season?)

### Dealing with NaNs

- interpolate using min/max/mean/median
- interpolate using a predictive model
- create new dummy variable/column (0 or 1) to indicate missing value for that param

## Modeling Ideas

### Model 1 Ideas

- `datetime.timedelta` between request and host reply?
- all datetimes normalized by subtracting initial contact datetime 

### Model 2 Ideas

- is the message length proportional to acceptance rate in the control and treatment groups separately?

### Model 3 Ideas

- won't arbitrary modifications to the rules frustrate hosts?
- will hosts be more curt, less detailed, less honest and open if forced to reply more quickly?
- what if host needs to check something at the property before accepting/rejecting a request
- what if host is unavailable out of town
- doesn't host know best how to "sell" their house using persuasion techniques like brinkmanship (to make it harder for guest to find an alternative)
