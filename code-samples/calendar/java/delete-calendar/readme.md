# java-delete-calendar

This sample will show you to easily delete a calendar with the Nylas Kotlin/Java beta SDK.

## Project Folder Structure

```text
code-samples
├── ...
├── calendar                   
│   ├── java          
│       ├── delete-calendar
│                        ├── DeleteCalendar.kt
│                        ├── readme.md
│                        ├── pom.xml                                                        
│   └── ...              
└── ...
```

## Setup

### System dependencies

- Kotlin 1.7

### Install dependencies

```xml
<dependency>
    <groupId>com.nylas.sdk</groupId>
    <artifactId>nylas</artifactId>
    <version>2.0.0-beta.1</version>
</dependency>
```

## Usage

Run the DeleteCalendar `.kt` on your IDE or to run on terminal, execute below maven command along with pom `.xml` and DeleteCalendar in the current working directory:

```bash
mvn exec:java  -Dexec.mainClass=DeleteCalendar
```

When the calendar is successfully deleted, you'll get the id of deleted calendar object in the terminal :

```text
Calendar [ ... ]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  8.116 s
[INFO] Finished at: 2023-10-31T13:29:33+05:30
[INFO] ------------------------------------------------------------------------
```

## Learn more

Visit our [Nylas Java SDK documentation](https://developer.nylas.com/docs/developer-tools/sdk/java-sdk/) to learn more.
