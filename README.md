# Formik and Form Validation

## Learning Goals

- Learn how to create and validate forms with Formik and Yup.

***

## Key Vocab

- **Validation**: Validation is an automatic check to ensure that data entered is sensible and feasible.
- **Form**: An HTML form is used to collect user input. The user input is most often sent to a server for processing.

***

## Introduction

Working with Form data on the front end can be tricky. We need to use the correct form html elements, write logic to validate data, and handle submissions. Formik is a React library that makes working with forms easy for us.

A full working solution is provided in the client directory. To start the server run `npm install` and `npm start` in the client directory. The site will be running on `http://localhost:3000/`

## Sign up form

In this lesson we will create a sign up form using React and Formik.
The form will include input fields for email, name and age.

Lets look at the `Signup.js` file which contains the sign up form component.

The Formik library provides us a hook to give initial values to the form and write a `onSubmit` callback function to do something with the values that were submitted. We can use the `onSubmit` method to submit
the values to an API or store the values in any way we want. In this example we will use show the JSON data in an alert on the page so we can see what the data model looks like. To do validation we can define a
`validationSchema` which we will look at later on in the lesson.

```js
  const formik = useFormik({
    initialValues: {
      name: "",
      email: "",
      age:"",
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
      alert(JSON.stringify(values, null, 2));
    },
  });
```

Lets look at the JSX we need to write for the form. The form looks similar to a form we may create without any libraries. The useFormik hook gives us many useful functions to pass into the HTML attributes. Note how we
do not have to write our own handleChange functions or logic to handle validation errors. The useFormik hook will do alot of that work for us. We can get values using `formik.values` and errors using `formik.errors`.

```js
  return (
    <form onSubmit={formik.handleSubmit} style={{margin:'30px'}}>
      <label htmlFor="email">Email Address</label>
      <input
        id="email"
        name="email"
        onChange={formik.handleChange}
        value={formik.values.email}
      />
      <p style={{color:'red'}}> {formik.errors.email}</p>
      <label htmlFor="name">Name</label>

      <input
        id="name"
        name="name"
        onChange={formik.handleChange}
        value={formik.values.name}
      />
      <p style={{color:'red'}}> {formik.errors.name}</p>

      <label htmlFor="age">age</label>

      <input
        id="age"
        name="age"
        onChange={formik.handleChange}
        value={formik.values.age}
      />
      <p style={{color:'red'}}> {formik.errors.age}</p>
      <button type="submit">Submit</button>
    </form>
  );
```

***

## Validation

For validation we will use the Yup library that meshes well with Formik.
Yup is a JavaScript schema builder for value parsing and validation

Lets look at the validation schema.
Yup allows us to instantiate an object and define its shape using the shape function which takes in an object
of the fields we want to validate. We can chain validation rules to strict validation rules that allow us to
control input and create more robust applications.

```js
  const formSchema = yup.object().shape({
    email: yup.string().email("Invalid email"),
    name: yup.string().required("Must enter a name").max(15),
    age: yup.number().positive().integer().required("Must enter age").typeError('Please enter an Integer').max(125),
  })
```

Lets look at the age schema. We want to accept a `number()` which is `positive()` and is an `integer()`. We also want to make sure it is `required()`. Yup makes error messages easy to work with. We can pass the error message we want to display in the broken rule by passing a string into the rule definition like we did here `required("Must enter age")`.

We can access these errors in the JSX by using the formik hooks errors attribute
`<p style={{color:'red'}}> {formik.errors.name}</p>`. In this example we show the validation errors as a
red `<p>` tag.

Now imagine how difficult it would be to write all the logic needed for the validation and error handling if we needed to do with without formik.

***

## Conclusion

 In this lesson we covered the basic functionality of creating a form and validating some inputs. With Formik we can create a more robust application and make sure we don't submit data to an API that may be unexpected or incorrect. This lesson was meant to show how Formik works at a fundamental level. The code we wrote is very explicit about exactly what Formik is doing. If you want to reduce the boilerplate code even more you can use front end components that wire the forms for us. Learn more about the built in Formik form components here [less verbose forms](https://formik.org/docs/overview#reducing-boilerplate).

***

## Complete code

```js
import React from "react";
import { useFormik } from "formik";
import * as yup from "yup"
export const SignupForm = () => {
  // Pass the useFormik() hook initial form values and a submit function that will
  // be called when the form is submitted
  const formSchema = yup.object().shape({
    email: yup.string().email("Invalid email"),
    name: yup.string().required("Must enter a name").max(15),
    age: yup.number().positive().integer().required("Must enter age").typeError('Please enter an Integer').max(125),
  })

  const formik = useFormik({
    initialValues: {
      name: "",
      email: "",
      age:"",
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
      alert(JSON.stringify(values, null, 2));
    },
  });


  return (
    <form onSubmit={formik.handleSubmit} style={{margin:'30px'}}>
      <label htmlFor="email">Email Address</label><br/>
      <input
        id="email"
        name="email"
        onChange={formik.handleChange}
        value={formik.values.email}
      />
      <p style={{color:'red'}}> {formik.errors.email}</p>
      <label htmlFor="name">Name</label><br/>

      <input
        id="name"
        name="name"
        onChange={formik.handleChange}
        value={formik.values.name}
      />
      <p style={{color:'red'}}> {formik.errors.name}</p>

      <label htmlFor="age">age</label><br/>

      <input
        id="age"
        name="age"
        onChange={formik.handleChange}
        value={formik.values.age}
      />
      <p style={{color:'red'}}> {formik.errors.age}</p>
      <button type="submit">Submit</button>
    </form>
  );
};

```

## Resources

- [Formik](https://formik.org/docs/tutorial)
- [Formik Validation](https://formik.org/docs/guides/validation)
- [React](https://reactjs.org/docs/hello-world.html)
