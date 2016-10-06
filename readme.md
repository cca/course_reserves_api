# Course Reserves API

Instructors place particular titles—books and movies—on _reserve_ during the semester, meaning that the titles cannot be checked out for long periods but instead are held in the library for use in shorter increments of time (often a mere two hours). This project documents how the libraries exposes structured data about the current semester's course reserves in JSON.

## Request Structure

Requests are made to a URL of form: https://library.cca.edu/cgi-bin/koha/svc/report?id=155&sql_params=SSHIS-200&sql_params=03

Breaking this down:

- https://library.cca.edu/cgi-bin/koha/svc/report is the base URL, this is a path on the library catalog server running [Koha](https://koha-community.org/)
- the "id" query string parameter is always "155"<sup>\*</sup>
- two "sql_params" parameters follow
    + the first is the course code e.g. five capital letters followed by hyphen & a three-digit number, e.g. "ARCHT-507"
    + the second is the _section_ number e.g. a two-digit number (with padded zeroes for the numbers 1-9)
    + **both parameters are required** but if the second is left empty (e.g. `&sql_params=SSHIS-200&sql_params=`) then reserves for _all_ sections of the same course code are returned

<sup>\*</sup> 155 is the _report ID_. If the libraries build similar APIs exposing other catalog data in the future, the report ID parameter for those will differ.

## Response Structure

The JSON response looks like this:

```js
[
    [
        "Monster : the autobiography of an L.A. gang member / Sanyika Shakur, aka Monster Kody Scott.",
        "https://library.cca.edu/cgi-bin/koha/opac-detail.pl?biblionumber=42697"
    ],
    [
        "Do androids dream of electric sheep? / Philip K. Dick.",
        "https://library.cca.edu/cgi-bin/koha/opac-detail.pl?biblionumber=42694"
    ],
    [
        "One hundred demons / by Lynda Barry.",
        "https://library.cca.edu/cgi-bin/koha/opac-detail.pl?biblionumber=53548"
    ]
]
```

That is, the response is an array of arrays. Each child array represents one title being held on reserve and has two items: the first is a title/author string and the second is the catalog URL for that title.

## Notes

An example client application "ex.py" written in Python is included for reference:

```sh
> ./ex.py SSHIS-200 03 >> reserves.html
```

It writes an HTML list of links to the reserve titles to stdout.

This is just a first draft of the API. The libraries can add further data fields to the output arrays as needed, as well as structure the request differently. We are limited in that the output will always be a array of arrays and not objects with informative property names, and the request structure will always involve a series of `sql_params` parameters which also cannot be given informative names.

## LICENSE

[ECL Version 2.0](https://opensource.org/licenses/ECL-2.0)
