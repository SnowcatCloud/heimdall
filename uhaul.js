
  var context = [
    {
      schema: "iglu:com.uhaul/ui/jsonschema/1-0-0",
      data: {
        id: "unique-group-id",
        name: "Group Name",
      },
    },
  ];

  window.snowplow("trackPageView", { context });

