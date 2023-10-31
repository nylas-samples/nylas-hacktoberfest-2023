# java-delete-grant

This sample will show you to easily delete a grant with the Nylas Kotlin/Java beta SDK.

## Project Folder Structure

```text
code-samples
├── ...
├── calendar                   
│   ├── java          
│       ├── delete-grant
│                        ├── DeleteGrant.kt
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

Run the DeleteGrant `.kt` on your IDE or to run on terminal, execute below maven command along with pom `.xml` and DeleteGrant in the current working directory:

```bash
mvn exec:java  -Dexec.mainClass=DeleteGrant
```

When the grant is successfully deleted, you'll get the id of deleted grant object in the terminal :

```text
Grant [ ... ]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  8.220 s
[INFO] Finished at: 2023-10-31T7:18:23+05:30
[INFO] ------------------------------------------------------------------------
```

## Learn more

Visit our [Nylas Java SDK documentation](https://developer.nylas.com/docs/developer-tools/sdk/java-sdk/) to learn more.
