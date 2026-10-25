# Content schema

The renderer accepts UTF-8 JSON. Required fields are `meta`, `orientation`, and non-empty `chapters`. Other arrays may be empty. Stable IDs use lowercase letters, digits, and hyphens.

```json
{
  "meta": {"title":"Book title","author":"Author","edition":"Edition","source_file":"Source","coverage":"complete","coverage_note":"Processed scope","generated_at":"YYYY-MM-DD","theme":{"accent":"#9E2A24"}},
  "orientation": {"eyebrow":"Author · domain","thesis":"One faithful sentence","problem":"Problem addressed","reader":"Who benefits","how_to_read":"Reading path"},
  "coverage_map": [{"range":"p. 1-29","chapter_id":"ch-01","status":"read","quality":"high","notes":"Checked against page images"}],
  "overview": [{"id":"arc-01","title":"Arc","summary":"Role in the book","details":["Stage and claim","Transition and consequence"],"related_concepts":["concept-a"],"anchors":["p. 12-35"]}],
  "chapters": [{"id":"ch-01","title":"Chapter","question":"Question answered","role":"Why it exists","mainline":"Connected account of the chapter's argument","sections":[{"title":"Subargument","detail":"Mechanism, evidence, example and qualification","excerpts":[{"text":"Short exact excerpt","anchor":"p. 18"}],"anchors":["p. 16-21"]}],"argument_flow":["Premise","Mechanism","Conclusion"],"takeaways":["Point"],"related_concepts":["concept-a"],"anchors":["p. 12-29"],"confidence":"high"}],
  "concepts": [{"id":"concept-a","title":"Concept","one_line":"Definition","explanation":"Depth","factors":[{"name":"Factor","detail":"How it changes the concept","anchors":["p. 48"]}],"effects":["What it changes"],"observables":["What to look for"],"boundary":"Where it does not apply","relations":[{"target_id":"concept-b","label":"leads to","explanation":"Mechanism connecting the concepts"}],"excerpts":[{"text":"Short exact excerpt","anchor":"p. 48"}],"anchors":["p. 48"],"voice":"author","confidence":"high"}],
  "formulations": [{"text":"Short quotation or formulation","commentary":"Why it matters","anchors":["p. 61"],"verbatim":true}],
  "critique": [{"title":"Boundary","analysis":"Evaluation","anchors":["p. 70-74"],"voice":"editor"}],
  "reality": [{"question":"Observable question","application":"How to use it","anchors":["ch. 5"]}],
  "actions": [{"title":"Action","trigger":"When","steps":["Step"],"signal":"Expected evidence","review":"What to revisit"}],
  "glossary": [{"term":"Term","definition":"Meaning in this book","anchors":["p. 18"]}],
  "notes": ["Extraction or editorial note"]
}
```

`coverage_map` is required for a complete result. A partial prototype may omit it or contain pending rows, but `meta.coverage` must remain `partial`.

`chapters[].mainline` should be readable as a coherent explanation, not a label. `sections` preserves the source order and carries the concrete mechanisms, examples, evidence, limitations, and short excerpts needed to understand the chapter.

`concepts[].relations[].target_id` must resolve to another `concepts[].id`. If the target is not yet established from the processed source, omit the relation or create a clearly marked pending concept with `confidence: low`.

Use printed PDF page numbers when matched reliably; otherwise use `PDF p. N`. For reflowable books use chapter and heading names.
