# Illustration Style Analysis

Use this reference only when illustration is the image’s primary medium. The goal is to separate what is depicted from how it is drawn, and to convert recognizable style into observable visual techniques rather than relying on artist names, school names, or vague mood words.

## 1. Style Fingerprint

Analyze the illustration’s style fingerprint through:

- Medium and rendering method: line drawing, flat color, cel shading, painterly rendering, watercolor, gouache, ink wash, pencil, charcoal, printmaking, collage, paper cut, vector, pixel art, or mixed technique.
- Line language: no outline, thin contour, thick contour, variable line weight, broken line, sketch line, ink-brush line, geometric line, or soft edge.
- Shape and anatomy language: realistic, simplified, geometric, rounded, elongated, chibi, exaggerated, symbolic, organic, or architectural.
- Value and lighting language: flat values, hard cel bands, soft blending, textured blocks, watercolor blooms, dry-brush marks, strong chiaroscuro, rim light, or diffuse ambient light.
- Color language: limited palette, complementary contrast, muted colors, pastel, high saturation, earth tones, neon accents, transparent layers, or paper-like color variation.
- Texture and detail distribution: clean digital surfaces, paper grain, brush texture, visible strokes, halftone dots, pigment granulation, scratches, noise, dense subject detail, or simplified background detail.

Do not confuse the style fingerprint with the subject content. The style fingerprint describes how the image is made; the subject description describes what the image contains.

## 2. Evidence Weighting

Prioritize style evidence in this order:

1. Repeated traits that appear across the whole image, such as line logic, value structure, or palette.
2. Traits that affect the silhouette and main subject, such as shape simplification, contour, or anatomy.
3. Traits that affect the surface, such as brush marks, paper texture, or rendering method.
4. Local decorative details, which should be included only when they are visually prominent or repeated.

Do not treat a single small mark as the defining style. Do not mistake a low-resolution artifact, compression noise, or image-generation defect for a deliberate technique.

## 3. Primary and Supporting Styles; Resolving Conflicts

Choose one primary style direction and at most two supporting techniques from the style fingerprint. The primary direction controls the medium, line, and modeling logic; supporting techniques may add color, texture, or post-processing, but must not compete for control.

When styles conflict, keep the side with stronger evidence, larger coverage, or a clearer effect on the subject, and remove the other side. Check especially for:

- Flat vector treatment combined with heavy oil-paint buildup
- No-outline treatment combined with thick black closed contours
- Hard cel-shaded layers combined with continuous watercolor bleeding
- Minimal low detail combined with extremely dense photorealistic texture across the frame
- Matte paper combined with intense plastic specular reflection
- Loose hand-drawn edges combined with mechanically uniform geometric line width

Do not replace observation by stacking artist names, art movements, or contradictory atmosphere words. Translate recognizable reference styles into line, shape, value, color, brushwork, texture, and detail distribution.

## 4. Illustration Visual Anchors

When extracting 3–5 reproduction-critical elements for an illustration, choose at least two style anchors and prioritize combinations from the following list:

- One primary medium or rendering method
- One line, shape, or value anchor
- One color or lighting anchor
- One brushwork, texture, or detail-distribution anchor
- When necessary, the composition or spatial relationship that most affects similarity

Put these anchors in the first third of the positive Prompt. Subject identity matters, but do not postpone all style anchors until after the subject and story description.

## 5. Information Weight in an Illustration Positive Prompt

Use the following organizational proportions only for illustration positive Prompts. They are writing weights, not requirements for mechanical counting:

- Approximately 35–45% describing the style fingerprint and key style anchors
- Approximately 20–30% describing subject appearance, action, clothing, or design
- Approximately 15–20% describing composition, viewpoint, lighting, and spatial layers
- The remaining content describing background, narrative relationships, specific mood, post-processing, and medium boundaries

First state the primary medium, line and shape language, value treatment, core palette, and key texture, then connect naturally to subject, composition, and scene. The final output must still follow `SKILL.md`’s default length, semantic consistency between the two languages, and two-section format.

## 6. Pre-Completion Check

Confirm internally that:

- The style fingerprint describes “how it is drawn” without repeating “what is depicted.”
- There is only one primary style direction, with no more than two compatible supporting techniques.
- The style anchors that most affect similarity appear in the first third.
- The description uses observable evidence about line, color, value, and texture rather than empty mood words.
- Photography parameters, 3D material logic, or rules from other types have not been forced into the illustration.
- No medium, texture, character, prop, or background element absent from the original image has been added.
